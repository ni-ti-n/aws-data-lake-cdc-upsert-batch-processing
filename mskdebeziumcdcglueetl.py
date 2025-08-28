import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import boto3
from delta.tables import DeltaTable
from pyspark.sql.functions import expr
from pyspark.sql.functions import *
from pyspark.sql.functions import col

## @params: [JOB_NAME]
#args = getResolvedOptions(sys.argv, ['JOB_NAME'])
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'database_name','table_name','input_dir','dest_dir'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

glue_client = boto3.client('glue')

database_name = args['database_name']
table_name =  args['table_name']
path_to_json = args['input_dir'] + "topics/"
path_to_newdelta = args['dest_dir'] + "blogdeltatable/"


dynamic_frame = glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": True},
        connection_type="s3",
        format="json",
        connection_options={"paths": [path_to_json], "recurse": True}, transformation_ctx="dynamic_frame_json"
    )
    
dyf_drop_fields = dynamic_frame.drop_fields(paths=["__op", "__source_ts_ms"])

try:
    response = glue_client.get_table(DatabaseName=database_name, Name=table_name)
    print("Delta table already exists in the Glue catalog.")
    

    cdc_df = dyf_drop_fields.toDF()

    delta_df1 = DeltaTable.forName(spark, f"{database_name}.{table_name}")

    final_df = delta_df1.alias("prev_df").merge(
        source=cdc_df.alias("append_df"),
        condition=expr("prev_df.cust_id = append_df.cust_id")
    ).whenMatchedDelete(condition = "append_df.__deleted = 'true'"
    ).whenMatchedUpdate(set={
        "prev_df.cust_id": col("append_df.cust_id"),
        "prev_df.name": col("append_df.name"),
        "prev_df.mktsegment": col("append_df.mktsegment")
    }).whenNotMatchedInsert(values={
        "prev_df.cust_id": col("append_df.cust_id"),
        "prev_df.name": col("append_df.name"),
        "prev_df.mktsegment": col("append_df.mktsegment")
    }).execute()

except glue_client.exceptions.EntityNotFoundException:
    print("Delta table does not exist in the Glue catalog.")
    # Convert DynamicFrame to DataFrame
    dyf_drop_fields_1 = dyf_drop_fields.drop_fields(paths=["__deleted"])
    delta_df = dyf_drop_fields_1.toDF()

    # Write DataFrame as a Delta table
    delta_df.write.format("delta").option("path", path_to_newdelta).saveAsTable(f"{database_name}.{table_name}")

    print("Delta table created in the Glue catalog.")

job.commit()

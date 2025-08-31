# CDC-based Upsert Sync for Data Lakes using AWS Glue, Amazon MSK & Open Table Formats

This repository serves as companion documentation for the AWS Big Data blog post:

**Synchronize data lakes with CDC-based UPSERT using open table format, AWS Glue, and Amazon MSK**  
(Read the blog post: [here](https://aws.amazon.com/blogs/big-data/synchronize-data-lakes-with-cdc-based-upsert-using-open-table-format-aws-glue-and-amazon-msk/))

## Overview

In modern data architectures, data lakes are essential for storing large volumes of structured and unstructured data. Change Data Capture (CDC) involves identifying and capturing modifications in a source database and delivering those changes downstream.

This blog illustrates how to:

- Capture CDC from Amazon RDS (MySQL) using MSK Connect with Debezium
- Stream raw CDC data to Amazon S3 via the Confluent S3 Sink Connector
- Export data into a data lake using AWS Glue ETL jobs and an open table format (Delta Lake, Apache Iceberg, or Apache Hudi)
- Query synchronized data via Amazon Athena

For those needing near-real-time processing, the blog also discusses using AWS Glue Streaming ETL to bypass batch processing and directly write CDC to your open table format.

## Architecture

![Architecture](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/07/29/1-2.png)

The solution architecture flows as follows:

1. **CDC Capture via MSK Connect**
   - Debezium connector captures changes in RDS MySQL.
   - Confluent S3 Sink Connector writes those changes to S3 as raw data.  

2. **AWS Glue Batch ETL**
   - Processes S3 raw layer.
   - Upserts data into a delta-style data lake (e.g., Delta Lake on S3).  

3. **Open Table Format Sync**
   - Uses open table formats (Delta Lake, Apache Iceberg, or Apache Hudi) for transactional consistency and UPSERT capability.  

4. **Query via Athena**
   - Amazon Athena runs SQL queries on the synchronized data lake for analytics.  

5. **Optional Real-Time Processing**
   - For real-time CDC processing, an AWS Glue streaming job can read directly from the Kafka topic and write into the open table format on S3.

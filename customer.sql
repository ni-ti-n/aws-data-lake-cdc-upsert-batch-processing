-- MySQL dump for customer table
--
-- Database: salesdb 
-- Table: CUSTOMER
-- ------------------------------------------------------

CREATE DATABASE IF NOT EXISTS salesdb;
use salesdb;
GRANT ALL PRIVILEGES  ON salesdb.* to master WITH GRANT OPTION;

--
-- Table structure for table `CUSTOMER`
--

DROP TABLE IF EXISTS `CUSTOMER`;

CREATE TABLE `CUSTOMER` (
  `CUST_ID` INT NOT NULL,
  `NAME` varchar(25) NOT NULL,
  `MKTSEGMENT` varchar(50) NOT NULL,
  PRIMARY KEY (`CUST_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping random data for table `CUSTOMER`
--

LOCK TABLES `CUSTOMER` WRITE;

INSERT INTO `CUSTOMER` VALUES (1,'Customer Name 1','Market Segment 7'),(2,'Customer Name 2','Market Segment 2'),(3,'Customer Name 3','Market Segment 6'),(4,'Customer Name 4','Market Segment 5'),(5,'Customer Name 5','Market Segment 10'),(6,'Customer Name 6','Market Segment 7'),(7,'Customer Name 7','Market Segment 5'),(8,'Customer Name 8','Market Segment 10'),(9,'Customer Name 9','Market Segment 8'),(10,'Customer Name 10','Market Segment 2'),(11,'Customer Name 11','Market Segment 4'),(12,'Customer Name 12','Market Segment 7'),(13,'Customer Name 13','Market Segment 7'),(14,'Customer Name 14','Market Segment 6'),(15,'Customer Name 15','Market Segment 3'),(16,'Customer Name 16','Market Segment 2'),(17,'Customer Name 17','Market Segment 8'),(18,'Customer Name 18','Market Segment 8'),(19,'Customer Name 19','Market Segment 2'),(20,'Customer Name 20','Market Segment 9'),(21,'Customer Name 21','Market Segment 4'),(22,'Customer Name 22','Market Segment 10'),(23,'Customer Name 23','Market Segment 7'),(24,'Customer Name 24','Market Segment 3'),(25,'Customer Name 25','Market Segment 1'),(26,'Customer Name 26','Market Segment 1'),(27,'Customer Name 27','Market Segment 7'),(28,'Customer Name 28','Market Segment 1'),(29,'Customer Name 29','Market Segment 8'),(30,'Customer Name 30','Market Segment 5');

UNLOCK TABLES;
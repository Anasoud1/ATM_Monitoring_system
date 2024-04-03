-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: atm_db
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ATM`
--

DROP TABLE IF EXISTS `ATM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ATM` (
  `atmId` int NOT NULL AUTO_INCREMENT,
  `atmName` varchar(45) DEFAULT NULL,
  `networkAddress` varchar(45) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `timezone` varchar(100) DEFAULT NULL,
  `subnet` varchar(45) DEFAULT NULL,
  `branchId` int DEFAULT NULL,
  `groupId` int DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `cash_level` decimal(10,2) DEFAULT NULL,
  `last_cash_replenishment` varchar(100) DEFAULT NULL,
  `software_version` varchar(50) DEFAULT NULL,
  `uptime` int DEFAULT NULL,
  PRIMARY KEY (`atmId`),
  KEY `branchId` (`branchId`),
  KEY `groupId` (`groupId`),
  CONSTRAINT `ATM_ibfk_1` FOREIGN KEY (`branchId`) REFERENCES `Branch` (`branchId`),
  CONSTRAINT `ATM_ibfk_2` FOREIGN KEY (`groupId`) REFERENCES `Group` (`groupId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ATM`
--

LOCK TABLES `ATM` WRITE;
/*!40000 ALTER TABLE `ATM` DISABLE KEYS */;
INSERT INTO `ATM` VALUES (1,'ATM 1 - Main Branch','192.168.1.10',34.0522,-118.244,'2024-03-05T12:00:00Z','255.255.255.0',1,1,'Online',10000.00,'2024-02-22T10:00:00Z','v1.2.3',36000),(2,'ATM 2 - City Center','192.168.2.20',34.0686,-118.335,'2024-03-05T12:00:00Z','255.255.255.0',2,2,'Offline',5000.00,'2024-02-15T09:00:00Z','v1.1.5',0),(3,'ATM 3 - Airport','172.16.0.30',34.0417,-118.244,'2024-03-05T12:00:00Z','255.255.0.0',3,1,'Under Maintenance',7500.00,'2024-03-04T15:00:00Z','v1.2.1',14400),(4,'ATM 4 - University Branch','10.0.1.10',34.0653,-118.244,'2024-03-05T12:00:00Z','255.255.255.0',5,3,'Online',8000.00,'2024-02-29T14:00:00Z','v1.3.0',86400),(5,'ATM 5 - East Branch','192.168.3.30',34.0812,-118.291,'2024-03-05T12:00:00Z','255.255.255.0',2,4,'Online',6000.00,'2024-03-02T16:00:00Z','v1.1.7',36000),(6,'ATM 6 - Shopping Mall','172.16.1.50',34.0582,-118.259,'2024-03-05T12:00:00Z','255.255.0.0',1,2,'Offline',4000.00,'2024-02-20T12:00:00Z','v1.2.2',0),(7,'ATM 7 - Hospital','10.10.1.20',34.0742,-118.313,'2024-03-05T12:00:00Z','255.255.255.0',4,3,'Under Maintenance',9000.00,'2024-03-01T10:00:00Z','v1.3.1',28800);
/*!40000 ALTER TABLE `ATM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AtmDevice`
--

DROP TABLE IF EXISTS `AtmDevice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AtmDevice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `atmId` int NOT NULL,
  `deviceId` int NOT NULL,
  `deviceStatus` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`,`atmId`,`deviceId`),
  KEY `atmId` (`atmId`),
  KEY `deviceId` (`deviceId`),
  CONSTRAINT `AtmDevice_ibfk_1` FOREIGN KEY (`atmId`) REFERENCES `ATM` (`atmId`),
  CONSTRAINT `AtmDevice_ibfk_2` FOREIGN KEY (`deviceId`) REFERENCES `Device` (`deviceId`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AtmDevice`
--

LOCK TABLES `AtmDevice` WRITE;
/*!40000 ALTER TABLE `AtmDevice` DISABLE KEYS */;
INSERT INTO `AtmDevice` VALUES (1,4,6,'Operational'),(2,1,3,'Operational'),(3,5,8,'Faulty'),(4,2,4,'Under Maintenance'),(5,3,5,'Faulty'),(6,1,2,'Under Maintenance'),(7,6,10,'Under Maintenance'),(8,5,9,'Operational'),(9,1,1,'Operational'),(10,4,7,'Under Maintenance'),(11,2,1,'Operational'),(12,6,11,'Operational'),(13,3,1,'Operational');
/*!40000 ALTER TABLE `AtmDevice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Branch`
--

DROP TABLE IF EXISTS `Branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Branch` (
  `branchId` int NOT NULL AUTO_INCREMENT,
  `branchName` varchar(50) DEFAULT NULL,
  `regionId` int DEFAULT NULL,
  PRIMARY KEY (`branchId`),
  KEY `regionId` (`regionId`),
  CONSTRAINT `Branch_ibfk_1` FOREIGN KEY (`regionId`) REFERENCES `Region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Branch`
--

LOCK TABLES `Branch` WRITE;
/*!40000 ALTER TABLE `Branch` DISABLE KEYS */;
INSERT INTO `Branch` VALUES (1,'Main Branch',1),(2,'Downtown Branch',1),(3,'West Coast Headquarters',2),(4,'Chicago Office',3),(5,'University Branch',2);
/*!40000 ALTER TABLE `Branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Device`
--

DROP TABLE IF EXISTS `Device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Device` (
  `deviceId` int NOT NULL AUTO_INCREMENT,
  `deviceModel` varchar(100) DEFAULT NULL,
  `deviceManufacturer` varchar(100) DEFAULT NULL,
  `deviceSerialNumber` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`deviceId`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Device`
--

LOCK TABLES `Device` WRITE;
/*!40000 ALTER TABLE `Device` DISABLE KEYS */;
INSERT INTO `Device` VALUES (1,'Cash Dispenser 5000','Acme Corporation','ACME-CD5000-12345'),(2,'Card Reader CR-700','GlobalTech','GT-CR700-54321'),(3,'Receipt Printer RP-200','ValuePrint','VP-RP200-98765'),(4,'Cash Acceptor CA-3000','SecureCash','SC-CA3000-01234'),(5,'Fingerprint Scanner FS-1000','BioTech Security','BTS-FS1000-33456'),(6,'Touchscreen Display TS-500','EasyTouch Solutions','ETS-TS500-78945'),(7,'PIN Pad PP-200 (older model)','Legacy Systems','LS-PP200-12345'),(8,'Cash Dispenser HD-8000 (high-capacity)','SecureCash','SC-HD8000-56789'),(9,'Card Reader CR-800 (contactless)','GlobalTech','GT-CR800-90123'),(10,'Thermal Camera TC-2000 (environmental monitoring)','EnviroTech','ET-TC2000-45678'),(11,'Voice Guidance Module VG-100','Accessibility Solutions','AS-VG100-78901');
/*!40000 ALTER TABLE `Device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ElectronicJournal`
--

DROP TABLE IF EXISTS `ElectronicJournal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ElectronicJournal` (
  `ejId` int NOT NULL AUTO_INCREMENT,
  `ejData` varchar(1000) NOT NULL,
  `atmId` int NOT NULL,
  `timestamp` varchar(100) NOT NULL,
  PRIMARY KEY (`ejId`),
  KEY `atmId` (`atmId`),
  CONSTRAINT `ElectronicJournal_ibfk_1` FOREIGN KEY (`atmId`) REFERENCES `ATM` (`atmId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ElectronicJournal`
--

LOCK TABLES `ElectronicJournal` WRITE;
/*!40000 ALTER TABLE `ElectronicJournal` DISABLE KEYS */;
INSERT INTO `ElectronicJournal` VALUES (1,'Network interface card (NIC) rebooted due to unresponsive state.',1,'2024-03-05T10:15:00Z'),(2,'Software update v1.2.4 downloaded and installed successfully. Reboot initiated.',2,'2024-03-05T12:00:00Z'),(3,'Disk space usage threshold exceeded (95%). Initiated disk cleanup procedures.',3,'2024-03-05T08:30:00Z'),(4,'Cash dispenser motor detected overheating. Disabling cash dispense functionality until further investigation.',4,'2024-03-05T14:22:00Z'),(5,'Receipt printer low on paper (20% remaining). Sending alert for paper refill.',5,'2024-03-05T16:05:00Z'),(6,'Application error encountered (code: ABC123). Restarting application service.',6,'2024-03-05T13:40:00Z'),(7,'ATM communication lost (ping timeout). Attempting to re-establish connection.',7,'2024-03-05T17:15:00Z'),(8,'System log rotated successfully. Old logs archived.',1,'2024-03-04T23:59:00Z'),(9,'Scheduled maintenance completed. System rebooted and services restarted.',3,'2024-03-05T06:00:00Z'),(10,'Security software detected suspicious activity. User attempted to access unauthorized functionality. Initiating investigation.',5,'2024-03-05T15:30:00Z');
/*!40000 ALTER TABLE `ElectronicJournal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Event` (
  `eventId` int NOT NULL AUTO_INCREMENT,
  `eventName` varchar(100) NOT NULL,
  `eventLevel` enum('INFO','WARNING','ERROR','CRITICAL') NOT NULL,
  `ejId` int DEFAULT NULL,
  PRIMARY KEY (`eventId`),
  UNIQUE KEY `eventName` (`eventName`),
  KEY `ejId` (`ejId`),
  CONSTRAINT `Event_ibfk_1` FOREIGN KEY (`ejId`) REFERENCES `ElectronicJournal` (`ejId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES (1,'Network Connectivity Issue','WARNING',1),(2,'Software Update','INFO',2),(3,'Cash Dispenser Malfunction','ERROR',3),(4,'Paper Refill Required','INFO',4),(5,'Card Reader Error','ERROR',5),(6,'Application Error','ERROR',6),(7,'ATM Communication Loss','CRITICAL',7),(8,'System Log Rotation','INFO',8),(9,'Scheduled Maintenance','INFO',9),(10,'Suspicious Activity Detected','CRITICAL',10);
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Group`
--

DROP TABLE IF EXISTS `Group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Group` (
  `groupId` int NOT NULL AUTO_INCREMENT,
  `groupName` varchar(100) DEFAULT NULL,
  `groupDescription` varchar(5000) DEFAULT NULL,
  `groupType` enum('Static','Dynamic') DEFAULT NULL,
  PRIMARY KEY (`groupId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Group`
--

LOCK TABLES `Group` WRITE;
/*!40000 ALTER TABLE `Group` DISABLE KEYS */;
INSERT INTO `Group` VALUES (1,'Hardware Issues','ATMs in this group are experiencing various hardware malfunctions, impacting user experience and potentially causing service outages. Common issues include cash dispenser jams, card reader errors, and receipt printer malfunctions.','Dynamic'),(2,'Network Connectivity Issues','ATMs in this group are unable to communicate with the central network due to various connectivity problems. This hinders transactions and might cause service outages for users. Potential causes include network outages at the provider\'s end, issues with the ATM\'s network card, or firewall configurations blocking communication.','Dynamic'),(3,'Software Glitches','ATMs in this group are exhibiting software-related issues, leading to unexpected behavior, system crashes, or specific functionalities being unavailable. These issues might require software updates or patches to resolve.','Dynamic'),(4,'Environmental Sensor Alerts','ATMs in this group have reported sensor readings exceeding recommended thresholds. While not causing immediate service outages, these alerts require investigation to prevent potential hardware damage or malfunctioning due to extreme temperatures, humidity, or other environmental factors.','Dynamic');
/*!40000 ALTER TABLE `Group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Region`
--

DROP TABLE IF EXISTS `Region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Region` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regionName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Region`
--

LOCK TABLES `Region` WRITE;
/*!40000 ALTER TABLE `Region` DISABLE KEYS */;
INSERT INTO `Region` VALUES (1,'East Coast'),(2,'West Coast'),(3,'Midwest');
/*!40000 ALTER TABLE `Region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaction`
--

DROP TABLE IF EXISTS `Transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transaction` (
  `transactionId` int NOT NULL AUTO_INCREMENT,
  `transactionType` varchar(45) NOT NULL,
  `transactionDetail` varchar(1000) DEFAULT NULL,
  `ejId` int DEFAULT NULL,
  PRIMARY KEY (`transactionId`),
  KEY `ejId` (`ejId`),
  CONSTRAINT `Transaction_ibfk_1` FOREIGN KEY (`ejId`) REFERENCES `ElectronicJournal` (`ejId`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaction`
--

LOCK TABLES `Transaction` WRITE;
/*!40000 ALTER TABLE `Transaction` DISABLE KEYS */;
INSERT INTO `Transaction` VALUES (1,'Withdrawal','User withdrew $100 from ATM ID: ATM001 at 2024-03-14 09:30:00',1),(2,'Withdrawal','User withdrew $50 from ATM ID: ATM002 at 2024-03-14 10:15:00',1),(3,'Deposit','User deposited $200 into ATM ID: ATM003 at 2024-03-14 11:00:00',2),(4,'Withdrawal','User withdrew $200 from ATM ID: ATM001 at 2024-03-14 12:45:00',1),(5,'Balance Inquiry','User checked balance at ATM ID: ATM002 at 2024-03-14 14:20:00',2),(6,'Withdrawal','User withdrew $20 from ATM ID: ATM003 at 2024-03-14 15:10:00',2),(7,'Withdrawal','User withdrew $80 from ATM ID: ATM004 at 2024-03-14 09:45:00',3),(8,'Withdrawal','User withdrew $200 from ATM ID: ATM005 at 2024-03-14 10:30:00',3),(9,'Deposit','User deposited $300 into ATM ID: ATM006 at 2024-03-14 11:20:00',4),(10,'Withdrawal','User withdrew $100 from ATM ID: ATM007 at 2024-03-14 12:15:00',4),(11,'Balance Inquiry','User checked balance at ATM ID: ATM008 at 2024-03-14 13:00:00',5),(12,'Withdrawal','User withdrew $50 from ATM ID: ATM009 at 2024-03-14 14:30:00',5),(13,'Deposit','User deposited $150 into ATM ID: ATM010 at 2024-03-14 15:05:00',6),(14,'Withdrawal','User withdrew $120 from ATM ID: ATM011 at 2024-03-14 16:00:00',6);
/*!40000 ALTER TABLE `Transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atm_cassettes`
--

DROP TABLE IF EXISTS `atm_cassettes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atm_cassettes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cassette_num` int DEFAULT NULL,
  `denomination` int DEFAULT NULL,
  `cassete_type` varchar(50) DEFAULT NULL,
  `num_bills` int DEFAULT NULL,
  `dispenserId` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dispenserId` (`dispenserId`),
  CONSTRAINT `atm_cassettes_ibfk_1` FOREIGN KEY (`dispenserId`) REFERENCES `AtmDevice` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atm_cassettes`
--

LOCK TABLES `atm_cassettes` WRITE;
/*!40000 ALTER TABLE `atm_cassettes` DISABLE KEYS */;
INSERT INTO `atm_cassettes` VALUES (1,1,100,'CASH CASSETTE',1000,9),(2,2,100,'CASH CASSETTE',958,9),(3,3,50,'CASH CASSETTE',600,9),(4,4,50,'CASH CASSETTE',1000,9),(5,1,100,'CASH CASSETTE',415,13),(6,2,100,'CASH CASSETTE',200,13),(7,3,50,'CASH CASSETTE',425,13),(8,4,50,'CASH CASSETTE',858,13);
/*!40000 ALTER TABLE `atm_cassettes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_atm`
--

DROP TABLE IF EXISTS `group_atm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group_atm` (
  `groupId` int NOT NULL,
  `atmId` int NOT NULL,
  PRIMARY KEY (`groupId`,`atmId`),
  KEY `atmId` (`atmId`),
  CONSTRAINT `group_atm_ibfk_1` FOREIGN KEY (`groupId`) REFERENCES `Group` (`groupId`),
  CONSTRAINT `group_atm_ibfk_2` FOREIGN KEY (`atmId`) REFERENCES `ATM` (`atmId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_atm`
--

LOCK TABLES `group_atm` WRITE;
/*!40000 ALTER TABLE `group_atm` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_atm` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-18 16:09:48

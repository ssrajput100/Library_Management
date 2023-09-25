-- MySQL dump 10.13  Distrib 5.5.16, for Win64 (x86)
--
-- Host: 127.0.0.1    Database: students
-- ------------------------------------------------------
-- Server version	5.5.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `Book_ID` char(10) NOT NULL DEFAULT '',
  `Book_Name` char(25) DEFAULT NULL,
  `Author` char(25) DEFAULT NULL,
  `Publisher` char(25) DEFAULT NULL,
  `Subject` char(20) DEFAULT NULL,
  `Class_Group` char(8) DEFAULT NULL,
  `Language` char(10) DEFAULT NULL,
  PRIMARY KEY (`Book_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('A4545B','Black Sun','Rebecca Roanhorse','Pan Macmillan','Science Fiction','9-12','English'),('A9067S','Bharat ki Khoj','Jawahar Lal Nehru','Scholastic','History','6-12','Hindi'),('B6937S','Vintage Sardar','Khushwant Singh','Penguin Evergreens','Classic','6-12','Hindi'),('C8654P','Knowledge','Daniel Mills','Penguin House','Encyclopedia','6-12','English'),('D5678V','Hind Swaraj','Mahatma Gandhi','The Floating Press','History','9-12','English'),('D6666G','Life is What You Make it','Preety Shenoy','Srishti Publications','Romance','11-12','English'),('F0109F','Haunted Museum','Suzanne Weyn','Scholastic','Horror','6-8','English'),('F7654Q','Why','Boyer','Nat Geography','Encyclopedia','6-12','English'),('G7836B','Old Man and The Sea','Earnest Hemmingway','Arrow Books','Fiction','8-12','English'),('H8907B','THUG','Angie Thomas','Penguin Publishers','Classic','9-12','English'),('J5880N','Gautam Buddha ki Kahaniya','Mukesh Nadan','Prabhat','Non-Fiction','6-12','Hindi'),('K7563M','Ask Me Anything','Shaila Brown','DK Publishers','Encyclopedia','6-12','English'),('L6789U','The Doors of Eden','Adrian Tchaikovsky','Pan Macmillan','Science Fiction','9-12','English'),('O4896L','Rebel Girls','Ellena Favilli','Particular Books','Arts','6-12','English'),('P9765Q','Boy and his Dreams','Vinita Krishna','Scholastic','Non-Fiction','6-12','English'),('R0987Y','The Story of My Life','Hellen Keller','Convent Publications','Autobiography','8-12','English'),('R3425F','Pride and Prejudice','Jane Austen','Bantam Classic','Classic','8-12','English'),('S0987E','Oliver Twist','Charles Dickens','Om Kidz','Classic','6-12','English'),('S7580V','Sardar Patel','Karam Das','Jainco','Biography','6-12','Hindi'),('S7634B','Mein Kampf','Adolf Hitler','Jaico','Autobiography','9-12','English'),('T6987L','Agni ki Udan','Arun Kumar Tiwari','Prabhat','History','8-12','Hindi'),('U0978J','Her Last Wish','Ajay Pandey','Srishti Publications','Non-Fiction','11-12','English'),('U7767E','David Copperfield','Charles Dickens','Penguin Publications','Classic','6-12','English'),('U9876P','Akbar Mahan','Vishmbhardatt Gaurh','New Sadhna','History','8-12','Hindi'),('V8745B','Meri Jeewan Yatra','Abdul Kalam','Prabhat','Autobiography','8-12','Hindi'),('W2341Q','The Alchemist','Panulo Coelho','Harper Collins','Science Fiction','8-12','English'),('W3068S','Believe in Yourself','Dr. Joseph Murphy','Manjul Publications','Psychology','10-12','English'),('X7490Y','Tree Tops','Jim Corbett','Oxford Press','Adventure','6-10','English'),('Y0987S','Joan of Arc','Hemlata Roy','Shree Book','Biography','6-10','English'),('Y5923P','The Quilt','Ismat Chugtai','Penguin Evergreens','Non-Fiction','8-12','English'),('Z4816D','Waiting for a Visa','B.R. Ambedkar','Xpress Publishers','Autobiography','8-12','English');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empl`
--

DROP TABLE IF EXISTS `empl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empl` (
  `empno` int(5) DEFAULT NULL,
  `ename` varchar(25) DEFAULT NULL,
  `job` varchar(15) DEFAULT NULL,
  `mgr` int(5) DEFAULT NULL,
  `hiredate` date DEFAULT NULL,
  `sal` decimal(10,0) DEFAULT NULL,
  `comm` decimal(10,0) DEFAULT NULL,
  `detno` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empl`
--

LOCK TABLES `empl` WRITE;
/*!40000 ALTER TABLE `empl` DISABLE KEYS */;
INSERT INTO `empl` VALUES (8369,'SMITH','CLERK',8902,'1990-12-18',800,NULL,20),(8499,'ANYA','SALESMAN',8698,'1991-02-20',1600,300,20),(8521,'SETH','SALESMAN',8698,'1991-02-22',1250,500,30),(8566,'MAHADEVAN','MANAGER',8839,'1991-04-02',2985,NULL,20),(8654,'MOMIN','SALESMAN',8698,'1991-09-28',1250,1400,30),(8698,'BINA','MANAGER',8839,'1991-05-01',2850,NULL,30),(8882,'SHIVANSH','MANAGER',8839,'1991-06-09',2450,NULL,10),(8888,'SCOTT','ANALYST',8566,'1992-12-09',3000,NULL,20),(8839,'AMIR','PRESIDENT',NULL,'1991-11-18',5000,NULL,10),(8844,'KULDEEP','SALESMAN',8698,'1991-09-08',1500,0,30),(8886,'ANOOP','CLERK',8888,'1993-01-02',1100,NULL,20),(8900,'JATIN','CLERK',8698,'1991-12-03',950,NULL,30),(8902,'FAKIR','ANALYST',8566,'1991-12-03',3000,NULL,20),(8934,'MITA','CLERK',8882,'1992-01-23',1300,NULL,10);
/*!40000 ALTER TABLE `empl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory` (
  `item` varchar(20) DEFAULT NULL,
  `quantity` int(3) DEFAULT NULL,
  `price` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('Lux',3,21),('oreo',2,20),('lays',10,10);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issued_books`
--

DROP TABLE IF EXISTS `issued_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issued_books` (
  `Book_ID` char(10) DEFAULT NULL,
  `Book_Name` char(25) DEFAULT NULL,
  `Student_ID` char(10) NOT NULL,
  `Student_Name` char(25) DEFAULT NULL,
  `Class` int(11) DEFAULT NULL,
  `Section` char(2) DEFAULT NULL,
  `Issued_Date` date DEFAULT NULL,
  `Last_Return_Date` date DEFAULT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issued_books`
--

LOCK TABLES `issued_books` WRITE;
/*!40000 ALTER TABLE `issued_books` DISABLE KEYS */;
INSERT INTO `issued_books` VALUES ('F7654Q','Why','B12500','Niya Sharma',11,'A','2020-07-12','2020-07-19'),('O4896L','Rebel Girls','B13524','Anshika Porwal',12,'A','2020-08-05','2020-08-12'),('D5678V','Hind Swaraj','B15000','Alaiza Shah',12,'A','2020-07-14','2020-07-21'),('F0109F','Haunted Museum','B20494','Aaliya Joanna',12,'A','2020-07-18','2020-07-25'),('U0978J','Her Last Wish','B24098','Shivam Agrawal',11,'A','2020-07-20','2020-07-27'),('Z4816D','Waiting for a Visa','B53321','Sara Baranwal',12,'B','2020-07-24','2020-08-01'),('S0987E','Oliver Twist','B67876','Mansi Soni',12,'B','2020-08-02','2020-08-09');
/*!40000 ALTER TABLE `issued_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recommended_books`
--

DROP TABLE IF EXISTS `recommended_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recommended_books` (
  `Student_ID` char(10) DEFAULT NULL,
  `Student_Name` char(25) DEFAULT NULL,
  `Class` int(11) DEFAULT NULL,
  `Section` char(2) DEFAULT NULL,
  `Book_Name` char(25) NOT NULL,
  `Author` char(25) DEFAULT NULL,
  PRIMARY KEY (`Book_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recommended_books`
--

LOCK TABLES `recommended_books` WRITE;
/*!40000 ALTER TABLE `recommended_books` DISABLE KEYS */;
INSERT INTO `recommended_books` VALUES ('B15000','Alaiza Shah',12,'A','Cafe Mystry','Scholatic'),('B15000','Alaiza Shah',12,'A','DCBGF','GVBJN'),('B90187','Ananya Singh',11,'B','Divergent','Veronica Roth'),('B45454','Srijan Verma',11,'B','Five Feet Apart','Rachael Lippincott'),('B54721','Mehul Bahnot',12,'A','Hamlet','Shakespeare'),('B53321','Sara Baranwal',12,'B','Harry Potter','J.K.Rowling'),('B12345','Abhijeet Pandey',11,'B','Huckelberry Finn','Charles Dickens'),('B50502','Vansh Jain',11,'A','Othello','Shakespeare'),('B40817','Rahul Gupta',11,'A','Sherlock Holmes','Arthur Conan Doyle'),('B90187','Ananya Singh',11,'B','Twilight Saga','Stephenie Meyer'),('B12500','Niya Sharma',11,'A','Wuthering Heights','Emily Bronte');
/*!40000 ALTER TABLE `recommended_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `returned_books`
--

DROP TABLE IF EXISTS `returned_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `returned_books` (
  `Book_ID` char(10) DEFAULT NULL,
  `Book_Name` char(25) DEFAULT NULL,
  `Student_ID` char(10) NOT NULL DEFAULT '',
  `Student_Name` char(25) DEFAULT NULL,
  `Class` int(11) DEFAULT NULL,
  `Section` char(2) DEFAULT NULL,
  `Issue_Date` date DEFAULT NULL,
  `Return_Date` date DEFAULT NULL,
  `Penalty` char(5) DEFAULT 'Null'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `returned_books`
--

LOCK TABLES `returned_books` WRITE;
/*!40000 ALTER TABLE `returned_books` DISABLE KEYS */;
INSERT INTO `returned_books` VALUES ('U9876P','Akbar Mahan','B15024','Aryan Tiwari',12,'A','2020-05-24','2020-05-29','0'),('W2341Q','The Alchemist','B23231','Anchit Hura',12,'B','2020-06-10','2020-06-20','150Rs'),('S7634B','Mein Kampf','B31130','Jiya James',11,'A','2020-05-22','2020-05-26','0'),('B6937S','Vintage Sardar','B46231','Akshara Tripathi',11,'B','2020-06-11','2020-06-13','0'),('S7580V','Sardar Patel','B53321','Sara Baranwal',12,'B','2020-06-15','2020-06-20','0'),('C8654P','Knowledge','B78912','Dhruv Gautam',12,'B','2020-05-28','2020-08-06','100Rs'),('U0978J','Her Last Wish','B93452','Niyali Kar',11,'B','2020-06-01','2020-06-08','0'),('Y5923P','The Quilt','B93452','Niyali Kar',11,'B','2020-07-28','2020-12-15','7000');
/*!40000 ALTER TABLE `returned_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_details`
--

DROP TABLE IF EXISTS `staff_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff_details` (
  `Staff_ID` char(10) NOT NULL,
  `Staff_Name` char(25) DEFAULT NULL,
  `Post` char(22) DEFAULT NULL,
  `Contact` bigint(20) DEFAULT NULL,
  `Gender` char(2) DEFAULT NULL,
  `Hire_Date` date DEFAULT NULL,
  `Salary_in_Rs` int(11) DEFAULT NULL,
  PRIMARY KEY (`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_details`
--

LOCK TABLES `staff_details` WRITE;
/*!40000 ALTER TABLE `staff_details` DISABLE KEYS */;
INSERT INTO `staff_details` VALUES ('AB2258','Pragyesh Pratabh','Library Head',9875683124,'M','1999-03-19',50000),('EF4099','Barnalee Sarkar','Junior Assistant',7651100920,'F','1995-04-24',25000),('GH0500','Ratan Kumar Singh','Security Guard',7654321098,'M','2014-04-14',12000);
/*!40000 ALTER TABLE `staff_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stud`
--

DROP TABLE IF EXISTS `stud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stud` (
  `NAME` varchar(20) DEFAULT NULL,
  `HOUSE` varchar(20) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `AGE` int(3) DEFAULT NULL,
  `GENDER` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud`
--

LOCK TABLES `stud` WRITE;
/*!40000 ALTER TABLE `stud` DISABLE KEYS */;
INSERT INTO `stud` VALUES ('sejal baranwal','kaveri','2003-11-28',16,'F'),('sara baranwal','kaveri','2006-06-13',14,'F'),('ananya singh','yamuna','2003-08-04',17,'F'),('vansh jain','narmada','2004-09-23',16,'M'),('jashnoor singh','yamuna','2003-03-03',17,'M'),('niyali kar','jhelum','2004-08-04',16,'F');
/*!40000 ALTER TABLE `stud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `name` char(20) DEFAULT NULL,
  `house` char(10) DEFAULT NULL,
  `age` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student1`
--

DROP TABLE IF EXISTS `student1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student1` (
  `name` varchar(20) DEFAULT NULL,
  `section` varchar(2) DEFAULT NULL,
  `house` varchar(15) DEFAULT NULL,
  `percent` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student1`
--

LOCK TABLES `student1` WRITE;
/*!40000 ALTER TABLE `student1` DISABLE KEYS */;
INSERT INTO `student1` VALUES ('rashi gupta','B','kaveri',95.8),('jerry smith','B','chenab',92),('akshara singh','C','jhelum',94.2),('kavya thakur','D','jhelum',90.4),('srijan verma','A','yamuna',98.2);
/*!40000 ALTER TABLE `student1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student2`
--

DROP TABLE IF EXISTS `student2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student2` (
  `studentno` int(3) DEFAULT NULL,
  `class` int(3) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `game` varchar(20) DEFAULT NULL,
  `grade1` varchar(2) DEFAULT NULL,
  `SUPW` varchar(20) DEFAULT NULL,
  `grade2` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student2`
--

LOCK TABLES `student2` WRITE;
/*!40000 ALTER TABLE `student2` DISABLE KEYS */;
INSERT INTO `student2` VALUES (10,7,'SAMEER','CRICKET','B','PHOTOGRAPHY','A'),(11,8,'SUJIT','TENNIS','A','GARDENING','C'),(12,7,'KAMAL','SWIMMING','B','PHOTOGRAPHY','B'),(13,7,'VEENA','TENNIS','C','COOKING','A'),(14,9,'ARCHANA','BASKETBALL','A','LITERATURE','A'),(15,10,'ARPIT','CRICKET','A','GARDENING','C');
/*!40000 ALTER TABLE `student2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_table`
--

DROP TABLE IF EXISTS `student_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_table` (
  `Student_ID` char(10) NOT NULL,
  `Student_Name` char(25) DEFAULT NULL,
  `Class` int(11) DEFAULT NULL,
  `Section` char(2) DEFAULT NULL,
  `Contact` bigint(20) DEFAULT NULL,
  `Gender` char(2) DEFAULT NULL,
  `Date_of_Birth` date DEFAULT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_table`
--

LOCK TABLES `student_table` WRITE;
/*!40000 ALTER TABLE `student_table` DISABLE KEYS */;
INSERT INTO `student_table` VALUES ('B12345','Abhijeet Pandey',11,'B',6664445556,'M','2004-06-28'),('B12500','Niya Sharma',11,'A',7897775643,'F','2004-03-11'),('B13524','Anshika Porwal',12,'A',7723148900,'F','2003-01-22'),('B15000','Alaiza Shah',12,'A',7688929241,'F','2003-07-21'),('B15024','Aryan Tiwari',12,'A',7683176823,'M','2003-08-12'),('B20494','Aaliya Joanna',12,'A',6987023651,'M','2002-12-11'),('B23231','Anchit Hura',12,'B',7878943431,'F','2003-06-13'),('B24098','Shivam Agrawal',11,'A',7894563218,'M','2004-10-15'),('B31130','Jiya James',11,'A',6000525212,'F','2003-11-30'),('B40817','Rahul Gupta',11,'A',7999848422,'M','2004-01-31'),('B45454','Srijan Verma',11,'B',9876543210,'M','2004-03-31'),('B46231','Akshit',11,'B',6862145266,'F','2004-09-29'),('B50502','Vansh Jain',11,'A',6364120388,'M','2004-09-07'),('B53321','Sara Baranwal',12,'B',7868699431,'F','2003-01-14'),('B54321','Sapna Singh',11,'A',9876543210,'F','2004-11-04'),('B54721','Mehul Bahnot',12,'A',6955907245,'M','2003-11-28'),('B58906','Vedanshi Dixit',12,'B',8343567431,'F','2003-06-15'),('B67876','Mansi Soni',12,'B',8279052391,'M','2003-10-19'),('B78912','Dhruv Gautam',12,'B',7897896789,'M','2003-02-28'),('B90187','Ananya Singh',11,'B',9425224433,'F','2003-08-04'),('B93452','Niyali Kar',11,'B',9454768742,'F','2004-08-04'),('WD4321','Pallavi Roy',12,'A',7896663512,'F','2003-03-03');
/*!40000 ALTER TABLE `student_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-30  0:52:02

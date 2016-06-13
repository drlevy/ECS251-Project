-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: test_db
-- ------------------------------------------------------
-- Server version	5.7.12-log

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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` bigint(20) NOT NULL DEFAULT '0',
  `post_id` bigint(20) NOT NULL DEFAULT '0',
  `page_id` bigint(20) NOT NULL DEFAULT '0',
  `fb_id` bigint(20) DEFAULT NULL,
  `message` text,
  `can_remove` tinyint(1) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`page_id`,`post_id`,`id`),
  KEY `comment_id` (`id`),
  KEY `fb_id` (`fb_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,1,0,1,'this is very bad',NULL,'0000-00-00 00:00:00'),(2,1,0,1,'this is a test. this test is very bad!',NULL,'0000-00-00 00:00:00'),(3,1,0,2,'this is the best ever',NULL,'0000-00-00 00:00:00'),(4,1,0,3,'i love this so much',NULL,'0000-00-00 00:00:00'),(5,2,0,1,'this is embarassing',NULL,'0000-00-00 00:00:00');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fb_user`
--

DROP TABLE IF EXISTS `fb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fb_user` (
  `id` bigint(20) NOT NULL,
  `name` text,
  `category` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fb_user`
--

LOCK TABLES `fb_user` WRITE;
/*!40000 ALTER TABLE `fb_user` DISABLE KEYS */;
INSERT INTO `fb_user` VALUES (1,NULL,NULL),(2,NULL,NULL),(3,NULL,NULL);
/*!40000 ALTER TABLE `fb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likedby`
--

DROP TABLE IF EXISTS `likedby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likedby` (
  `page_id` bigint(20) NOT NULL,
  `post_id` bigint(20) NOT NULL,
  `comment_id` bigint(20) NOT NULL DEFAULT '0',
  `fb_id` bigint(20) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`page_id`,`post_id`,`comment_id`,`fb_id`),
  KEY `fb_id` (`fb_id`),
  KEY `comment_id` (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likedby`
--

LOCK TABLES `likedby` WRITE;
/*!40000 ALTER TABLE `likedby` DISABLE KEYS */;
/*!40000 ALTER TABLE `likedby` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` bigint(20) NOT NULL DEFAULT '0',
  `page_id` bigint(20) NOT NULL DEFAULT '0',
  `from_id` bigint(20) NOT NULL,
  `message` text,
  `type` varchar(256) DEFAULT NULL,
  `picture` varchar(256) DEFAULT NULL,
  `story` text,
  `link` text,
  `link_name` text,
  `link_description` text,
  `link_caption` text,
  `icon` varchar(256) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `can_remove` tinyint(1) DEFAULT NULL,
  `shares_count` int(11) DEFAULT NULL,
  `likes_count` int(11) DEFAULT NULL,
  `comments_count` int(11) DEFAULT NULL,
  `entr_pg` float DEFAULT NULL,
  `entr_ug` float DEFAULT NULL,
  `object_id` varchar(40) DEFAULT NULL,
  `status_type` varchar(256) DEFAULT NULL,
  `source` varchar(256) DEFAULT NULL,
  `is_hidden` tinyint(1) DEFAULT NULL,
  `application_id` bigint(20) DEFAULT NULL,
  `place_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`page_id`,`id`),
  KEY `post_id` (`id`),
  KEY `created_time_index` (`created_time`),
  KEY `comments_count_index` (`comments_count`),
  KEY `from_id_index` (`from_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,0,0,'test is bad',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,0,0,'thing is good',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00','0000-00-00 00:00:00',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-12 17:33:10

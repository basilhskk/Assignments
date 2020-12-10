-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.20 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table ekplogismiko.adonis_schema
CREATE TABLE IF NOT EXISTS `adonis_schema` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `batch` int DEFAULT NULL,
  `migration_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Dumping data for table ekplogismiko.adonis_schema: ~9 rows (approximately)
/*!40000 ALTER TABLE `adonis_schema` DISABLE KEYS */;
INSERT INTO `adonis_schema` (`id`, `name`, `batch`, `migration_time`) VALUES
	(1, '1503248427885_user', 1, '2020-05-19 07:41:57'),
	(2, '1503248427886_token', 1, '2020-05-19 07:41:57'),
	(3, '1578478604748_categories_schema', 1, '2020-05-19 07:41:57'),
	(4, '1578478796892_products_schema', 1, '2020-05-19 07:41:58'),
	(5, '1580644030584_user_schema', 1, '2020-05-19 07:41:58'),
	(6, '1589884826463_product_schema', 2, '2020-05-19 13:40:56'),
	(7, '1589971560853_product_schema', 3, '2020-05-20 13:49:31'),
	(8, '1591563200800_report_schema', 4, '2020-06-07 23:58:58'),
	(9, '1591802187634_report_schema', 5, '2020-06-10 18:17:10');
/*!40000 ALTER TABLE `adonis_schema` ENABLE KEYS */;

-- Dumping structure for table ekplogismiko.categories
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(190) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `categories_name_unique` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Dumping data for table ekplogismiko.categories: ~2 rows (approximately)
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` (`id`, `created_at`, `updated_at`, `name`) VALUES
	(1, NULL, NULL, 'Μάθημα'),
	(2, NULL, NULL, 'Αξιολόγηση');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;

-- Dumping structure for table ekplogismiko.products
CREATE TABLE IF NOT EXISTS `products` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(80) DEFAULT NULL,
  `description` varchar(190) DEFAULT NULL,
  `category_id` int unsigned DEFAULT NULL,
  `url` varchar(249) DEFAULT NULL,
  `lesson` text,
  PRIMARY KEY (`id`),
  KEY `products_category_id_foreign` (`category_id`),
  CONSTRAINT `products_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Dumping data for table ekplogismiko.products: ~21 rows (approximately)
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` (`id`, `created_at`, `updated_at`, `name`, `description`, `category_id`, `url`, `lesson`) VALUES
	(1, '2020-05-19 11:44:48', '2020-05-19 11:44:48', 'Προπαίδεια του 1', 'Μάθημα για την κατανόηση της προπαιδειας 1', 1, '/img/1.png.png', '1*1 = 1||1*2 = 2||1*3 = 3||1*4 = 4||1*5 = 5||1*6 = 6||1*7 = 7||1*8 = 8||1*9 = 9||1*10 = 10'),
	(2, '2020-05-19 11:45:13', '2020-05-19 11:45:13', 'Προπαίδεια του 2', 'Μάθημα για την κατανόηση της προπαιδειας 2', 1, '/img/2.png.png', '2*1 = 2||2*2 = 4||2*3 = 6||2*4 = 8||2*5 = 10||2*6 = 12||2*7 = 14||2*8 = 16||2*9 = 18||2*10 = 20'),
	(3, '2020-05-19 11:45:19', '2020-05-19 11:45:19', 'Προπαίδεια του 3', 'Μάθημα για την κατανόηση της προπαιδειας 3', 1, '/img/3.png.png', '3*1 = 3||3*2 = 6||3*3 = 9||3*4 = 12||3*5 = 15||3*6 = 18||3*7 = 21||3*8 = 24||3*9 = 27||3*10 = 30'),
	(4, '2020-05-19 11:45:27', '2020-05-19 11:45:27', 'Προπαίδεια του 4', 'Μάθημα για την κατανόηση της προπαιδειας 4', 1, '/img/4.png.png', '4*1 = 4||4*2 = 8||4*3 = 12||4*4 = 16||4*5 = 20||4*6 = 24||4*7 = 28||4*8 = 32||4*9 = 36||4*10 = 40'),
	(5, '2020-05-19 11:45:33', '2020-05-19 11:45:33', 'Προπαίδεια του 5', 'Μάθημα για την κατανόηση της προπαιδειας 5', 1, '/img/5.png.png', '5*1 = 5||5*2 = 10||5*3 = 15||5*4 = 20||5*5 = 25||5*6 = 30||5*7 = 35||5*8 = 40||5*9 = 45||5*10 = 50'),
	(6, '2020-05-19 11:45:39', '2020-05-19 11:45:39', 'Προπαίδεια του 6', 'Μάθημα για την κατανόηση της προπαιδειας 6', 1, '/img/6.png.png', '6*1 = 6||6*2 = 12||6*3 = 18||6*4 = 24||6*5 = 30||6*6 = 6||6*7 = 42||6*8 = 48||6*9 = 54||6*10 = 60'),
	(7, '2020-05-19 11:45:45', '2020-05-19 11:45:45', 'Προπαίδεια του 7', 'Μάθημα για την κατανόηση της προπαιδειας 7', 1, '/img/7.png.png', '7*1 = 7||7*2 = 14||7*3 = 21||7*4 = 28||7*5 = 35||7*6 = 6||7*7 = 49||7*8 = 56||7*9 = 63||7*10 = 70'),
	(8, '2020-05-19 11:45:51', '2020-05-19 11:45:51', 'Προπαίδεια του 8', 'Μάθημα για την κατανόηση της προπαιδειας 8', 1, '/img/8.png.png', '8*1 = 8||8*2 = 16||8*3 = 24||8*4 = 32||8*5 = 40||8*6 = 6||8*7 = 56||8*8 = 64||8*9 = 72||8*10 = 80'),
	(9, '2020-05-19 11:46:02', '2020-05-19 11:46:02', 'Προπαίδεια του 9', 'Μάθημα για την κατανόηση της προπαιδειας 9', 1, '/img/9.png.png', '9*1 = 9||9*2 = 18||9*3 = 27||9*4 = 26||9*5 = 45||9*6 = 6||9*7 = 63||9*8 = 72||9*9 = 81||9*10 = 90'),
	(10, '2020-05-19 11:46:09', '2020-05-19 11:46:09', 'Προπαίδεια του 10', 'Μάθημα για την κατανόηση της προπαιδειας 10', 1, '/img/10.png.png', '10*1 = 10||10*2 = 20||10*3 = 30||10*4 = 40||10*5 = 50||10*6 = 60||10*7 = 70||10*8 = 80||10*9 = 90||10*10 = 100'),
	(11, '2020-05-19 11:54:06', '2020-05-19 11:54:06', 'TEST  Προπαίδεια του 1', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 1', 2, '/img/1.png.png', '1*1 = 1||1*2 = 2||1*3 = 3||1*4 = 4||1*5 = 5||1*6 = 6||1*7 = 7||1*8 = 8||1*9 = 9||1*10 = 10'),
	(12, '2020-05-19 11:54:18', '2020-05-19 11:54:18', 'TEST  Προπαίδεια του 2', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 2', 2, '/img/2.png.png', '2*1 = 2||2*2 = 4||2*3 = 6||2*4 = 8||2*5 = 10||2*6 = 12||2*7 = 14||2*8 = 16||2*9 = 18||2*10 = 20'),
	(13, '2020-05-19 11:54:28', '2020-05-19 11:54:28', 'TEST  Προπαίδεια του 3', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 3', 2, '/img/3.png.png', '3*1 = 3||3*2 = 6||3*3 = 9||3*4 = 12||3*5 = 15||3*6 = 18||3*7 = 21||3*8 = 24||3*9 = 27||3*10 = 30'),
	(14, '2020-05-19 11:54:37', '2020-05-19 11:54:37', 'TEST  Προπαίδεια του 4', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 4', 2, '/img/4.png.png', '4*1 = 4||4*2 = 8||4*3 = 12||4*4 = 16||4*5 = 20||4*6 = 24||4*7 = 28||4*8 = 32||4*9 = 36||4*10 = 40'),
	(15, '2020-05-19 11:54:46', '2020-05-19 11:54:46', 'TEST  Προπαίδεια του 5', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 5', 2, '/img/5.png.png', '5*1 = 5||5*2 = 10||5*3 = 15||5*4 = 20||5*5 = 25||5*6 = 30||5*7 = 35||5*8 = 40||5*9 = 45||5*10 = 50'),
	(16, '2020-05-19 11:54:59', '2020-05-19 11:54:59', 'TEST  Προπαίδεια του 6', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 6', 2, '/img/6.png.png', '6*1 = 6||6*2 = 12||6*3 = 18||6*4 = 24||6*5 = 30||6*6 = 6||6*7 = 42||6*8 = 48||6*9 = 54||6*10 = 60'),
	(17, '2020-05-19 11:55:08', '2020-05-19 11:55:08', 'TEST  Προπαίδεια του 7', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 7', 2, '/img/7.png.png', '7*1 = 7||7*2 = 14||7*3 = 21||7*4 = 28||7*5 = 35||7*6 = 6||7*7 = 49||7*8 = 56||7*9 = 63||7*10 = 70'),
	(18, '2020-05-19 11:55:18', '2020-05-19 11:55:18', 'TEST  Προπαίδεια του 8', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 8', 2, '/img/8.png.png', '8*1 = 8||8*2 = 16||8*3 = 24||8*4 = 32||8*5 = 40||8*6 = 6||8*7 = 56||8*8 = 64||8*9 = 72||8*10 = 80'),
	(19, '2020-05-19 11:55:35', '2020-05-19 11:55:35', 'TEST  Προπαίδεια του 9', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 9', 2, '/img/9.png.png', '9*1 = 9||9*2 = 18||9*3 = 27||9*4 = 26||9*5 = 45||9*6 = 6||9*7 = 63||9*8 = 72||9*9 = 81||9*10 = 90'),
	(20, '2020-05-19 11:55:44', '2020-05-19 11:55:44', 'TEST Προπαίδεια του 10', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση της προπαιδειας του 10', 2, '/img/10.png.png', '10*1 = 10||10*2 = 20||10*3 = 30||10*4 = 40||10*5 = 50||10*6 = 60||10*7 = 70||10*8 = 80||10*9 = 90||10*10 = 100'),
	(21, NULL, NULL, 'TEST Αυτοαξιολόγησης', 'Επαναληπτικό τεστ αξιολογησης της κατανόηση όλων των προπαιδιών', 2, '/img/test.png', '1*1 = 1||1*2 = 2||1*3 = 3||1*4 = 4||1*5 = 5||1*6 = 6||1*7 = 7||1*8 = 8||1*9 = 9||1*10 = 10||2*1 = 2||2*2 = 4||2*3 = 6||2*4 = 8||2*5 = 10||2*6 = 12||2*7 = 14||2*8 = 16||2*9 = 18||2*10 = 20||3*1 = 3||3*2 = 6||3*3 = 9||3*4 = 12||3*5 = 15||3*6 = 18||3*7 = 21||3*8 = 24||3*9 = 27||3*10 = 30||4*1 = 4||4*2 = 8||4*3 = 12||4*4 = 16||4*5 = 20||4*6 = 24||4*7 = 28||4*8 = 32||4*9 = 36||4*10 = 40||5*1 = 5||5*2 = 10||5*3 = 15||5*4 = 20||5*5 = 25||5*6 = 30||5*7 = 35||5*8 = 40||5*9 = 45||5*10 = 50||6*1 = 6||6*2 = 12||6*3 = 18||6*4 = 24||6*5 = 30||6*6 = 6||6*7 = 42||6*8 = 48||6*9 = 54||6*10 = 60||7*1 = 7||7*2 = 14||7*3 = 21||7*4 = 28||7*5 = 35||7*6 = 6||7*7 = 49||7*8 = 56||7*9 = 63||7*10 = 70||8*1 = 8||8*2 = 16||8*3 = 24||8*4 = 32||8*5 = 40||8*6 = 6||8*7 = 56||8*8 = 64||8*9 = 72||8*10 = 80||9*1 = 9||9*2 = 18||9*3 = 27||9*4 = 26||9*5 = 45||9*6 = 6||9*7 = 63||9*8 = 72||9*9 = 81||9*10 = 90||10*1 = 10||10*2 = 20||10*3 = 30||10*4 = 40||10*5 = 50||10*6 = 60||10*7 = 70||10*8 = 80||10*9 = 90||10*10 = 100');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;

-- Dumping structure for table ekplogismiko.reports
CREATE TABLE IF NOT EXISTS `reports` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int unsigned DEFAULT NULL,
  `lesson` varchar(249) DEFAULT NULL,
  `count` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reports_user_id_foreign` (`user_id`),
  CONSTRAINT `reports_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Dumping data for table ekplogismiko.reports: ~30 rows (approximately)
/*!40000 ALTER TABLE `reports` DISABLE KEYS */;
INSERT INTO `reports` (`id`, `created_at`, `updated_at`, `user_id`, `lesson`, `count`) VALUES
	(1, NULL, '2020-06-10 22:28:34', 1, '1', 2),
	(2, NULL, '2020-06-10 22:28:34', 1, '2', 2),
	(3, NULL, NULL, 1, '3', 0),
	(4, NULL, '2020-06-10 22:28:34', 1, '4', 4),
	(5, NULL, '2020-06-10 22:28:34', 1, '5', 4),
	(6, NULL, '2020-06-10 22:28:34', 1, '6', 2),
	(7, NULL, '2020-06-10 22:28:34', 1, '7', 2),
	(8, NULL, '2020-06-10 22:28:34', 1, '8', 2),
	(9, NULL, NULL, 1, '9', 0),
	(10, NULL, '2020-06-10 22:28:34', 1, '10', 2),
	(22, NULL, NULL, 7, '1', 0),
	(23, NULL, NULL, 7, '2', 0),
	(24, NULL, NULL, 7, '3', 0),
	(25, NULL, NULL, 7, '4', 0),
	(26, NULL, NULL, 7, '5', 0),
	(27, NULL, NULL, 7, '6', 0),
	(28, NULL, NULL, 7, '7', 0),
	(29, NULL, NULL, 7, '8', 0),
	(30, NULL, NULL, 7, '9', 0),
	(31, NULL, NULL, 7, '10', 0),
	(32, NULL, NULL, 8, '1', 0),
	(33, NULL, NULL, 8, '2', 0),
	(34, NULL, NULL, 8, '3', 0),
	(35, NULL, NULL, 8, '4', 0),
	(36, NULL, NULL, 8, '5', 0),
	(37, NULL, NULL, 8, '6', 0),
	(38, NULL, '2020-06-11 15:50:50', 8, '7', 3),
	(39, NULL, NULL, 8, '8', 0),
	(40, NULL, '2020-06-11 15:50:50', 8, '9', 3),
	(41, NULL, NULL, 8, '10', 0);
/*!40000 ALTER TABLE `reports` ENABLE KEYS */;

-- Dumping structure for table ekplogismiko.tokens
CREATE TABLE IF NOT EXISTS `tokens` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned DEFAULT NULL,
  `token` varchar(190) NOT NULL,
  `type` varchar(80) NOT NULL,
  `is_revoked` tinyint(1) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tokens_token_unique` (`token`),
  KEY `tokens_user_id_foreign` (`user_id`),
  KEY `tokens_token_index` (`token`),
  CONSTRAINT `tokens_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Dumping data for table ekplogismiko.tokens: ~0 rows (approximately)
/*!40000 ALTER TABLE `tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `tokens` ENABLE KEYS */;

-- Dumping structure for table ekplogismiko.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `email` varchar(190) NOT NULL,
  `password` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `role` varchar(190) DEFAULT NULL,
  `otp` varchar(190) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_username_unique` (`username`),
  UNIQUE KEY `users_email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Dumping data for table ekplogismiko.users: ~4 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `username`, `email`, `password`, `created_at`, `updated_at`, `role`, `otp`) VALUES
	(1, 'teacher123', 'basilhskoutsokostas@gmail.com', '$2a$10$O4tCSVCRKcByqTxMZ7opiO8HseGDQ0DJmCc1DdRd.j5o6vKpcE5rS', '2020-05-19 11:37:46', '2020-05-19 11:37:46', 'admin', NULL),
	(2, 'testStudent', 'b@gmail.com', '$2a$10$O4tCSVCRKcByqTxMZ7opiO8HseGDQ0DJmCc1DdRd.j5o6vKpcE5rS', '2020-06-07 21:36:23', '2020-06-07 21:36:23', 'user', NULL),
	(7, 'wdsasda', 'b@g.com', '$2a$10$Y87OCjsUGjsjuhgEbq7CyO3ZFdhjoZJT1Kd9uRELsRb6njGUHZ0Me', '2020-06-11 15:30:44', '2020-06-11 15:30:44', 'user', NULL),
	(8, 'sdasd', 'b@g.cc', '$2a$10$OnDGNPSqtRxzmczdR3nU4u1D6/NT.a8.27yOsxJQ2XTFZU45j/fA6', '2020-06-11 15:50:03', '2020-06-11 15:50:03', 'user', NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

DROP DATABASE IF EXISTS `test`;

CREATE DATABASE `test` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `test`;

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `telephone` varchar(15) NOT NULL DEFAULT '',
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login_time` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  `ext1` int(11) NOT NULL DEFAULT '0',
  `ext2` int(11) NOT NULL DEFAULT '0',
  `ext3` varchar(100) DEFAULT NULL,
  `ext4` varchar(100) DEFAULT NULL,
  `ext5` varchar(100) DEFAULT NULL,
  `ext6` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `username_unique_key` (`username`),
  UNIQUE KEY `email_unique_key` (`email`),
  KEY `idx_cnt` (`email`),
  KEY `idx_last_login` (`last_login_time`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_auth_user_tp` (`telephone`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO user(`id`, `username`, `first_name`, `last_name`, `email`, `telephone`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login_time`, `created_at`) VALUES (1, 'bug', 'Bug', 'Zuo', 'flyzfq@163.com', '18234125967', '2b84343a964e6ab56f9c5a232fa4f5b0', 1, 1, 1, NOW(), NOW());
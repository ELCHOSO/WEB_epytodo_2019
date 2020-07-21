START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS epytodo;
USE epytodo;

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` INT(7) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(256) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  UNIQUE KEY `username` (`username`)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `task` (
  `task_id` INT(7) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `title` VARCHAR(256) NOT NULL,
  `begin` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end` datetime DEFAULT NULL,
  `status` enum('not started','in progress','done') NOT NULL DEFAULT 'not started'
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `user_has_task` (
  `id` INT(7) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `fk_user_id` INT(7) NOT NULL,
  `fk_task_id` INT(7) NOT NULL,
  KEY `fk_user_id` (`fk_user_id`),
  KEY `fk_task_id` (`fk_task_id`)
)ENGINE=InnoDB;

ALTER TABLE user_has_task
  ADD CONSTRAINT `fk_task_id` FOREIGN KEY (`fk_task_id`)
    REFERENCES `task` (`task_id`),
  ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`fk_user_id`)
    REFERENCES `user` (`user_id`);
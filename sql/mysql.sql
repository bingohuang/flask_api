CREATE DATABASE `restful_db`;

CREATE TABLE `restful_db`.`books` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL UNIQUE,
  `author` VARCHAR(255) NOT NULL,
  `publish_time` TIMESTAMP NOT NULL
);

-- Creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Id is INT unique, auto generated, can’t be null and is a primary key
-- State_id INT, can’t be null and must be FOREIGN KEY that references to id
CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`state_id` INT NOT NULL FOREIGN KEY (`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`),
	`name` VARCHAR(256) NOT NULL);

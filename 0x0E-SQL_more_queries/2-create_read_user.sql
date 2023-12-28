-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- Check and create database if doesnot exit.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- Check and create the user and set userpassword.
CREATE USER IF NOT EXITS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant the priviledges the select ones
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

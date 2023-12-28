-- Script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXITS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEDGES NO *.* TO 'user_0d_1'@'localhost';

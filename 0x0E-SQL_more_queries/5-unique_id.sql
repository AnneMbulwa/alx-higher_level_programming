--script that creates the table unique_id on your MySQL server.
--id is an INT with the default value 1 and must be unique
CREATE TABLE IF NOT EXITS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

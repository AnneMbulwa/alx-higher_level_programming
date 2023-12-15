--script that creates the table id_not_null on your MySQL server
--id should gave a default of 1
CREATE TABLE IF NOT EXITS id_not_null (id INT DEFAULT 1, name VARCHAR(256));

0x0E. SQL - More queries
1. creating new mysql user
    syntax CREATE USER <name> @ localhost
2. Grating permissions to the user
    use GRANT
    example;
        GRANT PRIVILEGE ON database.table TO 'username'@'host';
    use FLUSH to flush priviledge
    example;
        FLUSH PRIVILEGES;
    use SHOW GRANTS - review a user’s current permissions
    example;
        SHOW GRANTS FOR 'username'@'host';
    use DROP - delete a user
    example;
        DROP USER 'username'@'localhost';
3. Mysql Grant statement
    basic syntax for GRANT statements.
        GRANT privilege [,privilege],../*grant multiple privileges, you need to separate privileges by commas.*/
        ON privilege_level /*(determines the extent to which the privileges apply)*/
        TO account_name /*account name of the user to receive the priviledges*/
4. Mysql constraints.
    NOT NULL - ensures that a table cannot have null values
    UNIQUE - ensures that all data are unique in a column
    PRIMARY KEY -uniquely identifies each record in a database table.
    It is a special case of unique keys. Primary keys cannot be NULL,unique keys can be. 
    FOREIGN KEY -  It is a referential constraint between two tables. The foreign key identifies a column or a set of columns in one (referencing) table that refers to a column or set of columns in another (referenced) table.
    ENUM -  a string object with a value chosen from a list of permitted values.
    SET - can have zero or more values. Each of the values must be chosen from a list of permitted values.
5. join
->NATURAL JOIN keyword specifies that the attributes whose values will be matched between the two tables are those with matching names;
Types of joins.
        a) inner join
            example:
                SELECT cFirstName, cLastName, orderDate
                FROM customers INNER JOIN orders
                USING (custID);

        b) outer join
            example:
                SELECT cFirstName, cLastName, orderDate
                FROM customers c LEFT OUTER JOIN orders o
                ON c.custID = o.custID;

        c) cross join
            example:
                SELECT cFirstName, cLastName, orderDate
                FROM customers CROSS JOIN orders;

        d) self join

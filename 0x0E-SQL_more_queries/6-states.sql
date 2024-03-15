-- Task: Create database hbtn_0d_usa and table states with specified structure
-- MySQL Version: 8.0.25

-- Check if the database exists
SELECT COUNT(*)
FROM information_schema.schemata
WHERE schema_name = 'hbtn_0d_usa' INTO @db_exists;

-- If database doesn't exist, create it
IF @db_exists = 0 THEN
    CREATE DATABASE hbtn_0d_usa;
END IF;

-- Use the database
USE hbtn_0d_usa;

-- Check if the table exists
SELECT COUNT(*)
FROM information_schema.tables
WHERE table_schema = 'hbtn_0d_usa' AND table_name = 'states' INTO @table_exists;

-- If table doesn't exist, create it
IF @table_exists = 0 THEN
    CREATE TABLE states (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL
    );
END IF;

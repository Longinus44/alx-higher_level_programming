-- Task: Create database hbtn_0d_2 and user user_0d_2 with limited privileges
-- MySQL Version: 8.0.25

-- Check if the database exists
SELECT COUNT(*)
FROM information_schema.schemata
WHERE schema_name = 'hbtn_0d_2' INTO @db_exists;

-- If database doesn't exist, create it
IF @db_exists = 0 THEN
    CREATE DATABASE hbtn_0d_2;
END IF;

-- Check if the user exists
SELECT COUNT(*)
FROM mysql.user
WHERE user = 'user_0d_2' AND host = 'localhost' INTO @user_exists;

-- If user doesn't exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
END IF;

-- Grant SELECT privilege to the user on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

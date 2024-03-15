-- Task: Create MySQL user user_0d_1 with all privileges and set its password
-- MySQL Version: 8.0.25

-- Check if the user exists
SELECT COUNT(*)
FROM mysql.user
WHERE user = 'user_0d_1' AND host = 'localhost' INTO @user_exists;

-- If user doesn't exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;


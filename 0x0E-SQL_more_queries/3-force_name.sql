-- Task: Create the table force_name with specified structure
-- MySQL Version: 8.0.25

-- Check if the table exists
SELECT COUNT(*)
FROM information_schema.tables
WHERE table_schema = DATABASE() AND table_name = 'force_name' INTO @table_exists;

-- If table doesn't exist, create it
IF @table_exists = 0 THEN
    CREATE TABLE force_name (
        id INT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    );
END IF;

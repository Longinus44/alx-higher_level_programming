-- Task: Create the table unique_id with specified structure
-- MySQL Version: 8.0.25

-- Check if the table exists
SELECT COUNT(*)
FROM information_schema.tables
WHERE table_schema = DATABASE() AND table_name = 'unique_id' INTO @table_exists;

-- If table doesn't exist, create it
IF @table_exists = 0 THEN
    CREATE TABLE unique_id (
        id INT DEFAULT 1 UNIQUE,
        name VARCHAR(256)
    );
END IF;

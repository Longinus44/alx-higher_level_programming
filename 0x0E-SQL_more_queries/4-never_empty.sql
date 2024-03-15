-- Task: Create the table id_not_null with specified structure
-- MySQL Version: 8.0.25

-- Check if the table exists
SELECT COUNT(*)
FROM information_schema.tables
WHERE table_schema = DATABASE() AND table_name = 'id_not_null' INTO @table_exists;

-- If table doesn't exist, create it
IF @table_exists = 0 THEN
    CREATE TABLE id_not_null (
        id INT DEFAULT 1,
        name VARCHAR(256)
    );
END IF;

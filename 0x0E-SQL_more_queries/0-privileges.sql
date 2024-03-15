-- Task: List all privileges of MySQL users user_0d_1 and user_0d_2 on the server (localhost).
-- MySQL Version: 8.0.25

-- SQL Query to list privileges of specified users

SELECT
    user, 
    host, 
    db, 
    table_name, 
    column_name, 
    routine_name, 
    privilege_type 
FROM 
    mysql.db 
WHERE 
    (user = 'user_0d_1' OR user = 'user_0d_2');

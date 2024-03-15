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

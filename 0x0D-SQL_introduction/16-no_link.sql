-- Script that lists all records of a table
-- Query that lists all the records in the second_table
-- 	table that contain a value in the name field
SELECT score, name FROM second_table
WHERE name IS NOT NULL 
ORDER BY score DESC;

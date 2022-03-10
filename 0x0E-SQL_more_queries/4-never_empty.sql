-- Script that creates a table
-- Query that creates the table 'id_not_null' indicating a
--	default value in the id field
CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1,
name VARCHAR(256)
);

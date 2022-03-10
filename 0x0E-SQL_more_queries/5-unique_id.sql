-- Script that creates a table
-- Query that creates the 'unique_id' table with a unique idº
CREATE TABLE IF NOT EXISTS unique_id(
id INT UNIQUE DEFAULT 1,
name VARCHAR(256)
);

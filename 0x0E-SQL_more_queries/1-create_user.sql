-- Script that creates a new user on the MySQL server
-- Query that creates new user 'user_0d_1' with password user_0d_1_pwd and with all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Script that creates a database and a table
-- Query to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Query to create cities in hbtn_0d_usa whit 7 constrain
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities ( 
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id));

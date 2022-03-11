-- Script that lists all cities contained in the database.
-- Query to join 2 tables (cities and states)
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;

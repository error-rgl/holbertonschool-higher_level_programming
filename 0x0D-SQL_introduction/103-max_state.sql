-- Script that shows the maximum temperature by state
-- Query that shows the maximum temperature of each state of the temperatures table
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;

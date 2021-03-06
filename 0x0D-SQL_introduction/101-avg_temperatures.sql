-- Script that displays the average temperature
-- Query that shows the average temperature by city arranged in a DESC way.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

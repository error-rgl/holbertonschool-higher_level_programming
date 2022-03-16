-- Script that displays the average temperature.
-- Query showing the average temperature per city during 
-- 	July and August sorted by temperature (descending).
SELECT city, AVG(value) AS avg_tmp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

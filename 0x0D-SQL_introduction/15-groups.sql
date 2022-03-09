-- Script that lists the number of records with the same score
-- Query that lists the number of records with the same score from the second_table table.
SELECT score, COUNT(score) AS number 
FROM second_table 
GROUP BY score 
ORDER BY score;

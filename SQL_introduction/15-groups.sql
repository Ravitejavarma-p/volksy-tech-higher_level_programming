-- getting list of same scores in table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;  

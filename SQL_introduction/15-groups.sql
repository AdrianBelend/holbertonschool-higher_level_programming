-- Number by score
SELECT score, count(*) AS 'number' FROM second_table GROUP BY score ORDER BY score DESC;

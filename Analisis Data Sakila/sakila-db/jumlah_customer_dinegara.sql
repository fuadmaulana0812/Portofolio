-- Negara paling banyak customer
SELECT country AS negara, COUNT(country) AS jumlah
FROM city AS c
JOIN country as cu
ON c.country_id=cu.country_id
JOIN address AS ad
ON c.city_id=ad.city_id
GROUP BY country
ORDER BY jumlah DESC;
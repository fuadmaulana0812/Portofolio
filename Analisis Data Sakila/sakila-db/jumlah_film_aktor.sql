-- Aktor paling banyak main film
SELECT CONCAT(e.first_name," ",e.last_name) AS aktor, COUNT(d.actor_id) AS jumlah
FROM actor e
JOIN film_actor d
ON d.actor_id=e.actor_id
GROUP BY aktor
ORDER BY aktor;
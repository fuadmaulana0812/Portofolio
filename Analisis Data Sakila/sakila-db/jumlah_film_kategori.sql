-- Jumlah film berdasarkan kategori film
SELECT
e.name AS kategori,
COUNT(film_id) AS jumlah_film
FROM
category e
JOIN film_category d ON d.category_id=e.category_id
GROUP BY kategori;
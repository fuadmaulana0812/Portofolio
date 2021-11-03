-- Total banyaknya customer berdasarkan tanggal rental
SELECT DATE(a.rental_date) AS tanggal, COUNT(b.customer_id) AS total_customer
FROM (SELECT*FROM rental
WHERE rental_date NOT LIKE '2006-02-14%') a
JOIN customer b
ON a.customer_id=b.customer_id
GROUP BY tanggal ORDER BY tanggal;
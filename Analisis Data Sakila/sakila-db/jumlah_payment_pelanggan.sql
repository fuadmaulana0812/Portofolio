-- Pelanggan paling banyak payment
SELECT CONCAT(c.first_name ," ", c.last_name) AS customer, COUNT(payment_id) AS jumlah_payment
FROM payment as p
JOIN customer as c ON p.customer_id=c.customer_id
GROUP BY customer
ORDER BY customer;
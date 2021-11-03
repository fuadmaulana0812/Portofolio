-- Customer Status
SELECT 
CASE
WHEN active = 1 THEN 'Aktif'
ELSE 'Tidak Aktif'
END AS status, COUNT(active) AS jumlah
FROM customer
GROUP BY status;
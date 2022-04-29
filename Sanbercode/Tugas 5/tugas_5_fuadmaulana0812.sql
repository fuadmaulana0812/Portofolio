SELECT o.orderNumber, o.orderDate, c.customerName, c.city, c.country, od.quantityOrdered, p.productName
FROM customers c
INNER JOIN orders o ON c.customerNumber = o.customerNumber
INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber
INNER JOIN products p ON od.productCode = p.productCode
WHERE p.productName = "1992 Ferrari 360 Spider red"
AND o.orderDate BETWEEN "2004-08-01" AND "2004-12-01";
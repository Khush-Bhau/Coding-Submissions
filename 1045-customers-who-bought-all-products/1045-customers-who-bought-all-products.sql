SELECT c.customer_id
FROM Customer c
CROSS JOIN (SELECT COUNT(*) AS total FROM Product) t
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = MAX(t.total);


-- Q1: Top 10 customers by total spending

SELECT
    c.CustomerId,
    c.FirstName,
    c.LastName,
    ROUND(SUM(i.Total), 2) AS TotalSpent,
    COUNT(i.InvoiceId) AS InvoiceCount
FROM Customer c
INNER JOIN Invoice i
    ON c.CustomerId = i.CustomerId
GROUP BY
    c.CustomerId,
    c.FirstName,
    c.LastName
ORDER BY
    TotalSpent DESC,
    c.CustomerId ASC
LIMIT 10;

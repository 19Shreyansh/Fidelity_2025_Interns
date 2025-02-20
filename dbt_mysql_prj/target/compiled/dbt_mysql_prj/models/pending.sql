SELECT 
    c.customerName, 
    c.phone, 
    c.city, 
    c.country, 
    o.orderDate, 
    o.status, 
    p.productName, 
    od.quantityOrdered
FROM fidelity.customers c
JOIN fidelity.orders o ON c.customerNumber = o.customerNumber
JOIN fidelity.orderdetails od ON o.orderNumber = od.orderNumber
JOIN fidelity.products p ON od.productCode = p.productCode
WHERE o.status = 'Pending'
ORDER BY o.orderDate DESC
SELECT 
    c.customerName, 
    c.phone, 
    c.city, 
    c.state, 
    c.country, 
    o.orderDate, 
    o.status, 
    p.productName, 
    od.quantityOrdered
FROM fil_db.fil_schema.customers c
JOIN fil_db.fil_schema.orders o ON c.customerNumber = o.customerNumber
JOIN fil_db.fil_schema.orderdetails od ON o.orderNumber = od.orderNumber
JOIN fil_db.fil_schema.products p ON od.productCode = p.productCode
WHERE o.status = 'Pending'
ORDER BY o.orderDate DESC
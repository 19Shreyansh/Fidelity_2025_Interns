
  create view `fidelity`.`customerorder__dbt_tmp`
    
    
  as (
    SELECT 
    c.customerName, 
    c.phone, 
    c.city, 
    o.orderDate, 
    o.status
FROM 
    fidelity.customers c
JOIN 
    fidelity.orders o ON c.customerNumber = o.customerNumber
ORDER BY o.orderDate DESC
  );
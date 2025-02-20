
  create view `fidelity`.`nested__dbt_tmp`
    
    
  as (
    SELECT 
transaction_id, 
transaction_date, 
unit_price 
FROM fidelity.sales_db
WHERE unit_price > (
    SELECT AVG(unit_price) 
    FROM fidelity.sales_db
)
  );
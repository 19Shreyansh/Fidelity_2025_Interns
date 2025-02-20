
  create view `fidelity`.`sales__dbt_tmp`
    
    
  as (
    select
    transaction_id,
    transaction_date
from
    fidelity.sales_db
where
    quantity >= 4
  );
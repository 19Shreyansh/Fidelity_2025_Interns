
  create view `fidelity`.`date__dbt_tmp`
    
    
  as (
    select Date_format(
    transaction_date,'%Y-%m') as month,
    SUM(quantity*unit_price) as total
from
    fidelity.sales_db
group by 
    Date_format(transaction_date,'%Y-%m')
  );
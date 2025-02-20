
  create view `fidelity`.`sample__dbt_tmp`
    
    
  as (
    with rename_columns as (
    select
        customerNumber as customer_id,
        lower(customerName) as customer_name
    from 
        fidelity.customers
)

select * from rename_columns
  );
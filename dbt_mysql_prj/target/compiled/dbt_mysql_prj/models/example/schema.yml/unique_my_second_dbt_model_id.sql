
    
    

select
    id as unique_field,
    count(*) as n_records

from `fidelity`.`my_second_dbt_model`
where id is not null
group by id
having count(*) > 1



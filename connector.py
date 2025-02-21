from snowflake.connector import connect
import pandas as pd

con = connect(
    user="Shreyansh",
    password="Anonymous@785827",  
    account="jp31419.ap-southeast-1",
    warehouse="fil_wh",
    database="fil_db",
    schema="fil_schema",
    role="ACCOUNTADMIN"
)

cur = con.cursor()
cur.execute("SELECT * FROM fil_db.fil_schema.customers")

data = cur.fetchall()
df = pd.DataFrame(data, columns=[x[0] for x in cur.description]) 
print(df)

cur.close()
con.close()

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("oracle://sa0:sa0@localhost:1521/xe")
con = engine.connect()
# data.to_sql(name='test', con=con, if_exists='replace', index=False)
print(pd.read_sql_table(table_name='task', con=con))
# task_table = pd.read_sql_table(table_name='task', con=con)
# # task_table.describe()d
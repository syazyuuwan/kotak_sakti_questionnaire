#%% 
# import packages
import os
from queries import question_queries as qq
import numpy as np
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
#%%
# initialise connection variables
load_dotenv('.env')

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = "kotak_test"
#%%
# load data
customers_df = pd.read_csv("customers.csv") 
invoice_lines_df = pd.read_csv("invoice_lines.csv") 
invoices_df = pd.read_csv("invoices.csv") 
#%%
# create dictionaries
df_dict = {
    "customers":customers_df,
    "invoices":invoices_df,
    "invoice_lines":invoice_lines_df
}
query_dict = {
    "\nShow the number of customers purchasing more than 5 books":qq.query2,
    "\nShow the list of customers who never purchased anything":qq.query3,
    "\nShow the list of book purchased with the users":qq.query4
}
#%%
for df in df_dict:
    df_dict[df] = df_dict[df].replace([np.nan],[None])
#%%
# define function to execute queries
def run_query(query):
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

# define function to insert table from dataframe
def insert_table(table_name, table_df):
    insert_query = f"INSERT INTO {table_name} ({', '.join(table_df.columns)}) VALUES ({', '.join(['%s'] * len(table_df.columns))})"
    for index, row in table_df.iterrows():
        cursor.execute(insert_query, tuple(row))
#%%
# generate schema
with mysql.connector.connect(
    host=host,
    user=user,
    password=password
) as conn:

    with conn.cursor() as cursor:
        print("Generate schema")
        cursor.execute(f"CREATE SCHEMA {database};")
    conn.commit()

#%%
# generate tables
with mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database = database
) as conn:

    with conn.cursor() as cursor:
        print("Generate schema")
        cursor.execute(qq.query1)
#%%
# insert tables from df
with mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database = database
) as conn:

    with conn.cursor() as cursor:
        for df in df_dict:
            insert_table(df,df_dict[df])
    conn.commit()

#%%
# SQL queries
with mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database = database
) as conn:
    
    with conn.cursor() as cursor:
        for q in query_dict:
            print(q)
            print(run_query(query_dict[q]))

# %%

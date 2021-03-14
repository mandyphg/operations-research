import pandas as pd
import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, DateTime, Float
from amplpy import AMPL, DataFrame, Environment

# Connect to DB
serverDB = 'mssql://name_of_server?trusted_connection=yes;driver=SQL+Server+Native+Client+11.0'
engineDB = create_engine(serverDB).connect()

# retrieve staff requirement for the day from Database
query= """
SELECT *
  FROM [name_of_table]
 WHERE operation_date = ...
"""

staff_df = pd.read_sql(query, engineDB)
staff_df['HalfHour'] = staff_df['HalfHour'] * 10
staff_df['HalfHour'] = "H" + staff_df['HalfHour'].astype(int).astype(str).str.zfill(3)
staff_df_sum = staff_df.groupby(['HalfHour'])['StaffRequired'].sum()

import pandas as pd
import datetime
import urllib
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, DateTime, Float, PrimaryKeyConstraint
from amplpy import AMPL, DataFrame, Environment


# Connect to DB
server_name = 'MANDYXPS\SQLEXPRESS'
db_name = 'DATA'

params = urllib.parse.quote_plus('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=' + server_name + ';'
                                'Database=' + db_name + ';'
                                'Trusted_Connection=yes')

engine_db = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params).connect()

# retrieve staff requirement for the day from Database
query= """
SELECT *
  FROM [name_of_table]
 WHERE operation_date = ...
"""

staff_df = pd.read_sql(query, engine_db)
staff_df['HalfHour'] = staff_df['HalfHour'] * 10
staff_df['HalfHour'] = "H" + staff_df['HalfHour'].astype(int).astype(str).str.zfill(3)
staff_df_sum = staff_df.groupby(['HalfHour'])['StaffRequired'].sum()

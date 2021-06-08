#######################################################################
'''
run_all_ETL.py
----

Written in the Python 3.7.9 Environment

By Nicole Lund 

This Python script automatically runs all ETL steps for investigating
the holdings of 5 mutual funds.
'''
#######################################################################

# Import database password
import sys
sys.path.append(r"C:\Users\nlund\Documents\GitHub\untracked_files")
from postgres_pswd import user_remote, passwd_remote, host_remote

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy import create_engine

# Import Dependencies
import pandas as pd


#######################################################################
# Add all subfolders to search path
#######################################################################
# Append subfolder directories
sys.path.append('b_holdings_cleanup')
sys.path.append('c_sp500_scraping')
sys.path.append('d_database_diagram')
sys.path.append('e_sql_load')
sys.path.append('f_sql_analysis')


######################################################################
# Import Transformed Holdings Data
######################################################################
from holdings_clean import df_final as holdings_df

# Review holdings data transferred
print('')
print('----- Holdings DataFrame Tranfer Verification -----')
print(holdings_df.info())
# print(holdings_df.head())


#######################################################################
# Import Transformed S&P 500 Data
#######################################################################
from sp500_scrape import sp500_df

# Review S&P 500 data transferred
print('')
print('----- S&P 500 DataFrame Tranfer Verification -----')
print(sp500_df.info())
# print(sp500_df.head())


######################################################################
# Load DataFrames to PostgreSQL database
#######################################################################
from sql_load import load_sql

load_sql(user_remote, passwd_remote, host_remote)

# Create engine to mutual_funds
engine_startup = 'postgresql://' + user_remote + ":" + passwd_remote + "@" + host_remote + '/mutual_funds'
engine = create_engine(engine_startup)

sp500_df.to_sql(name='sp500', con=engine, if_exists='append')
holdings_df.to_sql(name='fund_holdings', con=engine, if_exists='append',index=False)

######################################################################
# Perform Analysis Queries in PostgreSQL database
#######################################################################


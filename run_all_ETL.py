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

# Import Dependencies
import sys
import pandas as pd

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy import create_engine

# Import database password
# Note: user needs to update postgres_pswd.py file with their database information or
# point to a personal untracked file
from postgres_pswd import host, database, username, passwd
if host == 'YOUR DATABASE HOST HERE':
    sys.path.append(r"C:\Users\nlund\Documents\GitHub\untracked_files")
    from postgres_remote import host, database, username, passwd

# Define how many sectors to display in the output of the sector analysis
output='top3'

# Create engine to mutual_funds database
engine_startup = 'postgresql://' + username + ":" + passwd + "@" + host + '/' + database
engine = create_engine(engine_startup)


#######################################################################
# Add all subfolders to search path
#######################################################################
sys.path.append('b_holdings_cleanup')
sys.path.append('c_sp500_scraping')
sys.path.append('d_database_diagram')
sys.path.append('e_sql_load')
sys.path.append('f_sql_analysis')


######################################################################
# Import Transformed Holdings DataFrame
######################################################################
from holdings_clean import df_final as holdings_df

# Review holdings data transferred
print('')
print('----- Holdings DataFrame Tranfer Verification -----')
print(holdings_df.info())


#######################################################################
# Import Transformed S&P 500 DataFrame
#######################################################################
from sp500_scrape import sp500_df

# Review S&P 500 data transferred
print('')
print('----- S&P 500 DataFrame Tranfer Verification -----')
print(sp500_df.info())


######################################################################
# Load DataFrames to PostgreSQL database
#######################################################################
# Creating the database tables
from sql_load import load_sql
load_sql(engine_startup)

# Load the database tables from the DataFrames
sp500_df.to_sql(name='sp500', con=engine, if_exists='append')
holdings_df.to_sql(name='fund_holdings', con=engine, if_exists='append')


######################################################################
# Perform Analysis Queries in PostgreSQL database
#######################################################################
# Analyze the database tables
from sql_analysis import analyze_sql
analyze_sql(engine_startup,output)

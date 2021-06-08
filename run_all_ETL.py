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
import pathlib
import sys
import pandas as pd


#######################################################################
# Add all subfolders to search path
#######################################################################
# Append subfolder directories
sys.path.append('1_holdings_cleanup')
sys.path.append('2_sp500_scraping')
sys.path.append('3_database_diagram')
sys.path.append('4_sql_load')
sys.path.append('5_sql_analysis')


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
# from sql_load import load_sql

# load_sql()


######################################################################
# Perform Analysis Queries in PostgreSQL database
#######################################################################


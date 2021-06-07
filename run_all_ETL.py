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

# Root Directory
workspace_path = pathlib.Path().absolute()
# print(f"workspace path: {workspace_path}")

# Subfolder Directories
holdings_cleanup_path = workspace_path.joinpath('1_holdings_cleanup')
print(f"Holdings Cleanup Path: {holdings_cleanup_path}")
sp500_scraping_path = workspace_path.joinpath('2_sp500_scraping')
database_diagram_path = workspace_path.joinpath('3_database_diagram')
sql_load_path = workspace_path.joinpath('4_sql_load')
sql_analysis_path = workspace_path.joinpath('5_sql_analysis')

# Append subfolder directories
sys.path.append(holdings_cleanup_path)
sys.path.append(sp500_scraping_path)
sys.path.append(database_diagram_path)
sys.path.append(sql_load_path)
sys.path.append(sql_analysis_path)
print(f"System Path: {sys.path}")


#######################################################################
# Import Transformed Holdings Data
#######################################################################
# from holdings_clean import df_final as holdings_df

# # Review holdings data transferred
# print('')
# print('----- Holdings DataFrame Tranfer Verification -----')
# print(holdings_df.head())


#######################################################################
# Import Transformed S&P 500 Data
#######################################################################
from sp500_scrape import sp500_df

# Review S&P 500 data transferred
print('')
print('----- S&P 500 DataFrame Tranfer Verification -----')
print(sp500_df.head())
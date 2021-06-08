#######################################################################
'''
sp500_scrape.py
----

Written in the Python 3.7.9 Environment

By Nicole Lund 

This Python script scrapes an html table of S&P500 companies from

Wikimedia Foundation. (2021, June 4). List of S&amp;P 500 companies. 
  Wikipedia. https://en.wikipedia.org/wiki/List_of_S%26P_500_companies. 

This script was converted from sp500_scrape.ipynb
'''
#######################################################################


# Import Dependencies
import pandas as pd

# Source URL
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Scrape tables from URL
tables_as_list = pd.read_html(url)

# Extract Table of Interest
full_sp500_df = tables_as_list[0]

# Remove Unneccesary Columns
sp500_df = full_sp500_df[['Symbol','Security','GICS Sector','GICS Sub-Industry']]

# Rename Columns and Set Index
sp500_df = sp500_df.rename(columns={'Symbol':'ticker','Security':'security_name','GICS Sector':'gics_sector','GICS Sub-Industry':'gics_sub_industry'})
sp500_df = sp500_df.set_index('ticker')
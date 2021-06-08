###################################################################
# holdings_clean.ipynb - Holdings file Clean
# by Tarak Patel
#
# This is Python script for cleanup of 5 Portfolio holdings excel file 
# downloaded from
# https://individuals.voya.com/product/variable-portfolio/holdings/monthly
#
# Then it combines all the df into one df to upload to SQL.
#
# This script was converted from holdings_clean.ipynb
####################################################################


# Dependencies and Setup
import pandas as pd
import numpy as ny


################ Voya Index Plus LargeCap Portfolio ########################
# Pull data 
data_index_LC = "a_source_data/voya-index-plus-largecap-portfolio-monthly-holdings-xls.xls"

# Read and store into Pandas data frame
read_index_LC = pd.read_excel(data_index_LC, skiprows=3)

index_LC_df = read_index_LC.dropna()
index_LC_df.insert(0, 'fund_name', 'Voya Index Plus LargeCap Portfolio')


################ Voya LargeCap Growth Portfolio ########################
data_LCG = "a_source_data/voya-large-cap-growth-portfolio-monthly-holdings-xls.xls"

# Read and store into Pandas data frame
read_LCG = pd.read_excel(data_LCG, skiprows=3)

LCG_df = read_LCG.dropna()
LCG_df.insert(0, 'fund_name', 'Voya LargeCap Growth Portfolio')


################ Voya LargeCap Value Portfolio ########################
# Pull data 
data_LCV = "a_source_data/voya-large-cap-value-portfolio-monthly-holdings-xls.xls"

# Read and store into Pandas data frame
read_LCV = pd.read_excel(data_LCV, skiprows=3)

LCV_df = read_LCV.dropna()
LCV_df.insert(0, 'fund_name', 'Voya LargeCap Value Portfolio')


################ Voya Russell LargeCap Index Portfolio ########################
# Pull data 
data_RLC = "a_source_data/voya-russell-large-cap-index-portfolio-monthly-holdings-xls.xls"

# Read and store into Pandas data frame
read_RLC = pd.read_excel(data_RLC, skiprows=3)

RLC_df = read_RLC.dropna()
RLC_df.insert(0, 'fund_name', 'Voya Russell LargeCap Index Portfolio')


################ Voya U.S. Stock Index Portfolio ########################
# Pull data 
data_USSI = "a_source_data/voya-us-stock-index-portfolio-monthly-holdings-xls.xls"

# Read and store into Pandas data frame
read_USSI = pd.read_excel(data_USSI, skiprows=3)

USSI_df = read_USSI.dropna()
USSI_df.insert(0, 'fund_name', 'Voya U.S. Stock Index Portfolio')


################ Voya U.S. Stock Index Portfolio ########################
# Use concate function to combine all dataframes.
df = pd.concat([index_LC_df, LCG_df, LCV_df, RLC_df, USSI_df])

# Column Names Clean up
df_final = df.rename(columns={'Ticker': 'ticker',
                     'Security Name' : 'security_name',
                     'Crncy' : 'currency',
                     'Country' : 'country',
                     'Price' : 'price',
                     'Quantity' : 'quantity',
                     'Market Value' : 'market_value',
                    })

# Reset the index to unique values
df_final = df_final.reset_index()
df_final = df_final[['fund_name','ticker','security_name','currency','country','price','quantity','market_value']]
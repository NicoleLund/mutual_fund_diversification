############################################################
# sql_analysis.ipynb
# ----
# 
# Written in the Python 3.7.9 Environment
# 
# By Nicole Lund 
# 
# This Jupyter Notebook analyzes the postgreSQL database.
# 
# The queries contained herin were developed in sql.sql and translated into sqlalchemy and pandas.
############################################################

# Import Dependencies
import sys
import pandas as pd

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

def analyze_sql(engine_startup,output=''):

    ############################################################
    # Access Database
    ############################################################

    # Create engine to mutual_funds database
    engine = create_engine(engine_startup)

    # reflect the existing database into a new model
    Base = automap_base()

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # View all of the classes that automap found
    Base.classes.keys()

    # Save references to each table
    sp500 = Base.classes.sp500
    holdings = Base.classes.fund_holdings

    # Create our session (link) from Python to the DB
    session = Session(bind=engine)

    ############################################################
    # Collect Total Market Value for each fund
    ############################################################

    # Query database
    result = session.query(\
        holdings.fund_name, func.sum(holdings.market_value)).\
        group_by(holdings.fund_name).\
        all()

    # Build Pandas DataFrame
    holdings_fund_name = []
    holdings_market_value = []
    for row in result:
        (fund_name, market_value) = row
        holdings_fund_name.append(fund_name)
        holdings_market_value.append(market_value)

    market_total_df = pd.DataFrame({'fund_name':holdings_fund_name,'total_market_value':holdings_market_value})

    market_total_df[['total_market_value']] = market_total_df[['total_market_value']].apply(pd.to_numeric)


    ############################################################
    # Collect SP 500 stocks for each fund
    ############################################################

    # Query database
    result = engine.execute('\
        SELECT fund_holdings.fund_name,\
            fund_holdings.ticker,\
            sp500.gics_sector,\
            fund_holdings.market_value\
        FROM   sp500\
        INNER  JOIN fund_holdings\
        ON     sp500.ticker = fund_holdings.ticker;\
        ')

    # Build Pandas DataFrame
    sp500_fund_name = []
    sp500_ticker = []
    sp500_gics_sector = []
    sp500_market_value = []
    for row in result:
        (fund_name, ticker, gics_sector, market_value) = row
        sp500_fund_name.append(fund_name)
        sp500_ticker.append(ticker)
        sp500_gics_sector.append(gics_sector)
        sp500_market_value.append(market_value)

    sp500_holdings_df = pd.DataFrame({'fund_name':sp500_fund_name, 'ticker':sp500_ticker, 'gics_sector':sp500_gics_sector, 'market_value':sp500_market_value})
    sp500_holdings_df[['market_value']] = sp500_holdings_df[['market_value']].apply(pd.to_numeric)


    ############################################################
    # Collect Total SP500 Market Value for each fund
    ############################################################

    sp500_market_total = sp500_holdings_df.groupby('fund_name').sum()
    sp500_market_total = sp500_market_total.rename(columns={'market_value':'sp500_market_value'})
    sp500_market_total


    ############################################################
    # Calculate percentage of SP 500 stock holdings
    ############################################################

    # Join market_value and sp_market_value analyses
    holdings_analysis_df = market_total_df.join(sp500_market_total, on='fund_name',how='left')

    # Calculate SP 500 holdings percentage 
    holdings_analysis_df['sp500_percentage'] = round(100*holdings_analysis_df['sp500_market_value']/holdings_analysis_df['total_market_value'],2)
    holdings_analysis_df = holdings_analysis_df.sort_values('sp500_percentage',ascending=False)

    # Convert market totals into millions
    holdings_analysis_df['total_market_value_MM'] = round(holdings_analysis_df['total_market_value']/1000000,3)
    holdings_analysis_df['sp500_market_value_MM'] = round(holdings_analysis_df['sp500_market_value']/1000000,3)

    # Remove unnecessary columns
    holdings_analysis_df = holdings_analysis_df[['fund_name','total_market_value_MM','sp500_market_value_MM','sp500_percentage']]

    # Set fund_name as index
    holdings_analysis_df = holdings_analysis_df.set_index('fund_name')
    print('')
    print('----- Fund S&P 500 Holdings Analysis -----')
    print(holdings_analysis_df)


    ############################################################
    # Collect top 3 Sectors for SP 500 stocks for each fund
    ############################################################

    # Collect Total Sector Value by fund
    sp500_sector_weight_df = sp500_holdings_df.groupby(['fund_name','gics_sector']).sum()
    sp500_sector_weight_df = sp500_sector_weight_df.rename(columns={'market_value':'sector_market_value'})

    # Sort funds by sector_market_value
    sp500_sector_weight_group_df = sp500_sector_weight_df['sector_market_value'].groupby('fund_name',group_keys=False)
    if output == 'top3':
        sp500_sector_weight_sort_df = sp500_sector_weight_group_df.apply(lambda x: x.sort_values(ascending=False).head(3))
    else:
        sp500_sector_weight_sort_df = sp500_sector_weight_group_df.apply(lambda x: x.sort_values(ascending=False))
    sp500_sector_weight_df = sp500_sector_weight_sort_df.to_frame()

    # Get total SP 500 Market Value for comparison
    sp500_market_value_list = []
    for row in sp500_sector_weight_df.iterrows():
        sp500_market_value_list.append(sp500_market_total.loc[row[0][0],'sp500_market_value'])
    sp500_sector_weight_df['sp500_market_value'] = sp500_market_value_list

    # Calculate SP500 sector percentage
    sp500_sector_weight_df['sector_percentage'] = round(100*sp500_sector_weight_df['sector_market_value']/sp500_sector_weight_df['sp500_market_value'],1)

    # Convert sector_market_value into millions
    sp500_sector_weight_df['sector_market_value_MM'] = round(sp500_sector_weight_df['sector_market_value']/1000000,3)

    # Collect relevant columns
    sp500_sector_weight_df = sp500_sector_weight_df[['sector_market_value_MM','sector_percentage']]

    print('')
    print('----- Fund S&P 500 Sector Analysis -----')
    print(sp500_sector_weight_df)

    ############################################################
    # Close Session
    ############################################################
    session.close()
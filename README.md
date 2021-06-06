# UofA Data Analytics Bootcamp Project 2 - ETL (Extract, Transform, Load)

**Team**:  Tarak Patel, Nicole Lund, and Anne Niemiec

-----

## Project Description
Investigate the types of stock holdings of 5 Mutual Funds including the percentage of stocks in the funds that are on the S&P 500 list and sub-categories of funds in each fund.

## Data Sources
* Mutual Fund Holdings Data (https://individuals.voya.com/product/variable-portfolio/holdings/monthly):  
    * Voya Index Plus Large Cap Excel File
    * Voya Large Cap Growth Excel File
    * Voya Large Cap Value Excel File
    * Voya Russell Large Cap Index Excel File
    * Voya US Stock Index Excel File
* S&P 500 Component Stocks HTML Table (https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) 

## Data Extraction Methods
* Mutual Fund Holdings Data: Extract individual Excel files with Pandas read_excel function
* S&P 500 Component Stocks Table: Extract HTML table with Pandas read_html function

## Data Transformation
* Mutual Fund Holdings DataFrame Tables: 
    * Remove 3 header rows
    * Remove NaNs
    * Add column with mutual fund holding name
    * Merge into one Pandas DataFrame via Pandas concat function
    * Set index to ticker and fund_name columns
* S&P 500  DataFrame Table:
    * Set index to ticker column
* All  DataFrame Tables
    * Confirm the data is clean
    * Rename columns to common format between both tables
    * Convert Jupyter notebooks to Python scripts for use with master run file

## Data Load
* Pre-plan database schema using https://app.quickdatabasediagrams.com/
* Use pandas and sqlalchemy to upload DataFrames to cloud-based SQL PostgreSQL database

-----

## Repository Structure
* 0_source_data: Downloaded mutual fund holdings Excel files
* 1_holdings_cleanup: Jupyter notebook converted into Python script for mutual fund holdings extraction and DataFrame cleanup
* 2_sp500_scraping: Jupyter notebook converted into Python script for S&P 500 extraction and DataFrame cleanup
* 3_database_diagram: Pre-planned PostgreSQL database schema scripts and diagram
* 4_sql_load: SQL database loading scripts
* 5_sql_analysis: SQL queries and database analysis

-----

## Citations
* Ltd, D. T. (n.d.). QuickDBD. QuickDatabaseDiagrams. https://app.quickdatabasediagrams.com/. 
* Monthly Variable Portfolio Holdings. Monthly Variable Portfolio Holdings | Voya Investment Management. (n.d.). https://individuals.voya.com/product/variable-portfolio/holdings/monthly.
* Wikimedia Foundation. (2021, June 4). List of S&amp;P 500 companies. Wikipedia. https://en.wikipedia.org/wiki/List_of_S%26P_500_companies. 
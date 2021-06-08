#######################################################################
'''
sql_load.py
----

Written in the Python 3.7.9 Environment

By Nicole Lund, Tarak Patel and Anne Niemiec

This Python script accesses the user defined database to delete 
any existing tables then initialize clean tables.

The postgreSQL queries for creating the tables was defined in
d_database_diagram\Schema.sql
'''
#######################################################################

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy import create_engine

def load_sql(engine_startup):
	# Create engine to mutual_funds
	engine = create_engine(engine_startup)

	# Create S&P 500 Table
	engine.execute('DROP TABLE IF EXISTS sp500 CASCADE; \
		CREATE TABLE "sp500" ( \
		"ticker" varchar(10)   NOT NULL, \
		"security_name" varchar(255)   NOT NULL, \
		"gics_sector" varchar(255)   NOT NULL, \
		"gics_sub_industry" varchar(255)   NOT NULL, \
		CONSTRAINT "pk_sp500" PRIMARY KEY ( \
			"ticker" \
		) \
	);')

	# Create holdings Table
	engine.execute('DROP TABLE IF EXISTS fund_holdings CASCADE; \
		CREATE TABLE "fund_holdings" ( \
		"index" varchar(10) PRIMARY KEY, \
		"fund_name" varchar(255)   NOT NULL, \
		"ticker" varchar(10)   NOT NULL, \
		"security_name" varchar(255)   NOT NULL, \
		"currency" varchar(5)   NOT NULL, \
		"country" varchar(50)   NOT NULL, \
		"price" decimal   NOT NULL, \
		"quantity" decimal   NOT NULL, \
		"market_value" decimal   NOT NULL\
	);')
-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/rQca87
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

--------------------------------------------------------------------------------
--
-- Schema.sql
-- 
-- By Anne Niemiec 
-- 
-- This file contains the SQL code for creating the tables defined in
-- quick_db)diagrams.txt
--
-- These queries were used in e_sql_load/sql_load.py
--
--------------------------------------------------------------------------------

CREATE TABLE "sp500" (
    "ticker" varchar(10)   NOT NULL,
    "security_name" varchar(255)   NOT NULL,
    "gics_sector" varchar(255)   NOT NULL,
    "gics_sub_industry" varchar(255)   NOT NULL,
    CONSTRAINT "pk_sp500" PRIMARY KEY (
        "ticker"
     )
);

CREATE TABLE "fund_holdings" (
    "index" varchar(10)   NOT NULL,
    "fund_name" varchar(255)   NOT NULL,
    "ticker" varchar(10)   NOT NULL,
    "security_name" varchar(255)   NOT NULL,
    "currency" varchar(5)   NOT NULL,
    "country" varchar(50)   NOT NULL,
    "price" decimal   NOT NULL,
    "quantity" decimal   NOT NULL,
    "market_value" decimal   NOT NULL,
    CONSTRAINT "pk_fund_holdings" PRIMARY KEY (
        "index"
     )
);

ALTER TABLE "fund_holdings" ADD CONSTRAINT "fk_fund_holdings_ticker" FOREIGN KEY("ticker")
REFERENCES "sp500" ("ticker");

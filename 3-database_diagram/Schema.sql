-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/rQca87
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

--------------------------------------------------------------------------------
--
-- quick_db_diagrams.txt
-- 
-- By Anne Niemiec 
-- 
-- This file contains the code for generating a DataBase Diagram from
--
-- https://app.quickdatabasediagrams.com/
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
    "ticker" varchar(10)   NOT NULL,
    "security_name" varchar(255)   NOT NULL,
    "currency" varchar(5)   NOT NULL,
    "country" varchar(50)   NOT NULL,
    "price" decimal   NOT NULL,
    "quantity" decimal   NOT NULL,
    "market_value" decimal   NOT NULL,
    "fund_name" varchar(255)   NOT NULL
);

ALTER TABLE "fund_holdings" ADD CONSTRAINT "fk_fund_holdings_ticker" FOREIGN KEY("ticker")
REFERENCES "sp500" ("ticker");


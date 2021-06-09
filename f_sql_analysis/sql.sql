------------
-- 
-- sql.sql
-- 
-- by Tarak Patel
-- 
-- This script analyzes the database tables within sql to 
-- assess the diversification of the mutual funds of interest.
--
------------

select * from sp500

---Create View for total Market value for funds
DROP VIEW IF EXISTS vw_total_fund_mv;

CREATE VIEW vw_total_fund_MV AS
SELECT fund_name, ROUND(SUM(market_value), 2) AS total_MV
FROM fund_holdings
GROUP BY fund_name
ORDER BY fund_name;

---SP 500 MV in Funds --- create view for Total MV for each fund that holds S&P 500 Securities.
DROP VIEW IF EXISTS vw_sp_MV_in_funds;

CREATE VIEW vw_sp_MV_in_funds AS
SELECT fh.fund_name, ROUND(SUM(fh.market_value), 2) AS sp_MV
FROM sp500 sp INNER JOIN fund_holdings fh 
ON sp.ticker = fh.ticker
GROUP BY fh.fund_name;

--- Calculating the % of SP500 stocks held by each Fund ---
select tf.fund_name, spmv.sp_mv, tf.total_mv, ROUND((spmv.sp_mv / tf.total_mv * 100), 2) AS "%_of_tmv"
from vw_total_fund_MV tf
INNER JOIN vw_sp_MV_in_funds spmv
on tf.fund_name = spmv.fund_name


---sector wieghts for SP 500 stocks for each fund---
SELECT fh.fund_name, sp.gics_sector, ROUND(SUM(fh.market_value), 2) AS sp_sector_MV, spmv.sp_mv
		, ROUND((SUM(fh.market_value) / spmv.sp_mv * 100), 2) AS "sector_weights_%_of_MV"
FROM sp500 sp INNER JOIN fund_holdings fh 
ON sp.ticker = fh.ticker 
INNER JOIN vw_sp_MV_in_funds spmv
ON fh.fund_name = spmv.fund_name
GROUP BY fh.fund_name, sp.gics_sector, spmv.sp_mv
ORDER by fund_name, sp_sector_mv desc;
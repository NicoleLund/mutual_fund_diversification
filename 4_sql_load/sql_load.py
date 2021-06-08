def load_sql():

	# Import database password
    import sys
    sys.path.append(r"C:\Users\nlund\Documents\GitHub\untracked_files")
    from postgres_pswd import user_remote, passwd_remote, host_remote

	# Python SQL toolkit and Object Relational Mapper
	import sqlalchemy
	from sqlalchemy import create_engine

	# Create engine to mutual_funds
	# engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
	engine_startup = 'postgresql://' + user_remote + ":" + passwd_remote + "@" + host_remote + '/mutual_funds'
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
		"ticker" varchar(10)   NOT NULL, \
		"security_name" varchar(255)   NOT NULL, \
		"currency" varchar(5)   NOT NULL, \
		"country" varchar(50)   NOT NULL, \
		"price" decimal   NOT NULL, \
		"quantity" decimal   NOT NULL, \
		"market_value" decimal   NOT NULL, \
		"fund_name" varchar(255)   NOT NULL, \
        FOREIGN KEY("ticker") REFERENCES "sp500" ("ticker") \
	);')

    print('Created tables in database')


if __name__ == '__main__':
    load_sql()
    

import sys


def get_ticher_symbols():

	COMPANIES = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "Tesla": "TSLA",
        "Nokia": "NOK",
    }
	STOCKS = {
        "AAPL": 287.73,
        "MSFT": 173.79,
        "NFLX": 416.90,
        "TSLA": 724.88,
        "NOK": 3.37,
    }

	def get_key(val):
		for key, value in COMPANIES.items():
			if val == value:
				return key

	if len(sys.argv) == 2:
		if COMPANIES.get(get_key(sys.argv[1].upper())):
			val = get_key(sys.argv[1].upper())
			l = STOCKS.get(sys.argv[1].upper())
			print(val, l, sep=' ')
		else:
			print("Unknown ticker")
	else:
		sys.exit(1)


if __name__=="__main__":
	get_ticher_symbols()
import sys

def	search_in_dict():

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

	if len(sys.argv) == 2:
		if (COMPANIES.get(sys.argv[1].capitalize())):
			l = COMPANIES.get(sys.argv[1].capitalize())
			print(STOCKS.get(l))
		else:
			print("Unknown company")
	else:
		sys.exit(1)


if __name__=="__main__":
	search_in_dict()

import sys

def	get_key_value():

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
		res = sys.argv[1].upper().strip().split(',')
		for elem in res:
			if elem == '' or elem.isspace():
				print()
				sys.exit(1)
		for elem in res:
			elem = elem.strip()
			if elem in STOCKS.keys():
				print(f"{elem} is a ticker symbol for {get_key(elem)}")
			else:
				if elem.capitalize() in COMPANIES.keys():
					print(f"{elem.capitalize()} stock price is {STOCKS.get(COMPANIES.get(elem.capitalize()))}")
				else:
					print(f"{elem.capitalize()} is an unknown company or an unknown ticker symbol")
	else:
		sys.exit(1)
	


if __name__=="__main__":
	get_key_value()
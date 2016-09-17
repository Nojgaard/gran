import quandl

data = quandl.get(["WIKI/FB.4", "WIKI/MSFT.4"], start_date="2015-06-01", end_date="2016-01-01")

print(data)

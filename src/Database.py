import quandl
import urllib.request
import xml.etree.ElementTree as ET
from Stock import Stock

# quandl api authentication
quandl.ApiConfig.api_key = '-b2fk-v3un2si3_FB18U'

def get_stocks(query = "", max_stocks = 10, database_code = "WIKI"):
    url = "https://www.quandl.com/api/v3/datasets.xml?database_code=" + database_code
    url = url + "&per_page=" + str(max_stocks) + "&page=1"
    if query != "":
        url = url + "&query=" + query.replace(" ", "+")

    req = urllib.request.urlopen(url)
    root = ET.fromstring(req.read());
    stocks = []
    for dataset in root.iter("dataset"):
        stock = Stock()
        for child in dataset:
            if child.tag == "name":
                stock.name = child.text
            elif child.tag == "dataset-code":
                stock.dataset_code = child.text
            elif child.tag == "database-code":
                stock.database_code = child.text
        stocks.append(stock)
    return stocks

def get_history(stocks, start, end):
    req_stocks = [x.code() + ".4" for x in stocks]
    data = quandl.get(req_stocks, start_date=start, end_date=end)
    data = data.dropna(axis = 1)
    return data

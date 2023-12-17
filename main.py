import datetime
import pandas as pd
from parameter import * 
import requests
import json

class stockdata:
    def __init__(self, ticker, module):
        self.ticker = ticker
        self.module = module
        self.path = path[module]
        self.apiurl = apiurl[module]
     
    def print_value(self):
        print(self.ticker)
        print(self.module)
        print(self.path)
        print(self.apiurl)

    def getdata(self):
        writer = pd.ExcelWriter(self.path, engine='xlsxwriter')

        for x in self.ticker:
            response = requests.get(self.apiurl.format(ticker[x], token))
            result = json.dumps(response.json(), sort_keys=True)
            dict = json.loads(result)
            finaldf = pd.json_normalize(dict)
            finaldf.to_excel(writer, sheet_name=x)

        writer.close()


if __name__ == '__main__':
    
    for x in modulelist:
        e = stockdata(ticker, x)
        # e.print_value()
        e.getdata()
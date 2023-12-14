import datetime
import pandas as pd
from parameter import * 
import requests
import json

def getIEXCloudData():
    writer = pd.ExcelWriter(path[stockprice], engine='xlsxwriter')

    for x in ticker:
        response = requests.get("https://cloud.iexapis.com/stable/stock/{}/chart/1y?token={}".format(ticker[x], token))
        stockresult = json.dumps(response.json(), sort_keys=True)
        stockdict = json.loads(stockresult)
        stockresultdf = pd.json_normalize(stockdict) 
        stockresultdf.to_excel(writer, sheet_name=x)

    writer.close()

def getCorporateActions():
    writer = pd.ExcelWriter(path[news], engine='xlsxwriter')

    for x in ticker:
        response = requests.get("https://cloud.iexapis.com/stable/stock/{}/news/last/10?token={}".format(ticker[x], token))
        newsresult = json.dumps(response.json(), sort_keys=True)
        newsdict = json.loads(newsresult)
        newsresultdf = pd.json_normalize(newsdict) 
        newsresultdf.to_excel(writer, sheet_name=x)

    writer.close()

def getFundamentalValuations():
    writer = pd.ExcelWriter(path[key], engine='xlsxwriter')

    for x in ticker:
        response = requests.get("https://cloud.iexapis.com/stable/time-series/FUNDAMENTAL_VALUATIONS/{}?token={}".format(ticker[x], token))
        keyresult = json.dumps(response.json(), sort_keys=True)
        keydict = json.loads(keyresult)
        keyresultdf = pd.json_normalize(keydict) 
        keyresultdf.to_excel(writer, sheet_name=x)

    writer.close()

if __name__ == '__main__':

    getIEXCloudData()
    getCorporateActions()
    getFundamentalValuations()

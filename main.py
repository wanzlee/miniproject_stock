import datetime
import pyEX as iex
import pandas as pd
from parameter import * 


def GetIEXCloudData():
    client = iex.Client(api_token=token)
    writer = pd.ExcelWriter(path, engine='xlsxwriter')

    for x in ticker:
        stockprice = client.chartDF(ticker[x])
        stockprice.to_excel(writer, sheet_name=x)

    writer.close()

if __name__ == '__main__':

    GetIEXCloudData()
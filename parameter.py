import datetime

modulelist = ["stockprice", "news", "key"]
token = ***
ticker ={ 
            "Boeing": "BA",
            "Apple": "aapl",
            "Tesla": "tsla",
            "Alphabet": "goog",
            "Airbnb": "abnb"
        }
tdy = datetime.datetime.now().strftime("%d%b%Y")
path = {
            "stockprice" : "./data/IEXStockPrice_{}.xlsx".format(tdy),
            "news" : "./data/IEXNews_{}.xlsx".format(tdy),
            "key" : "./data/IEXKeyPerformance_{}.xlsx".format(tdy)
       }
apiurl = {
            "stockprice" : "https://cloud.iexapis.com/stable/stock/{}/chart/1y?token={}",
            "news" : "https://cloud.iexapis.com/stable/stock/{}/news/last/10?token={}",
            "key" : "https://cloud.iexapis.com/stable/time-series/FUNDAMENTAL_VALUATIONS/{}?token={}"
       }

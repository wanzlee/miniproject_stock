import datetime

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
            "stockprice" : './data/IEXStockPrice_{}.xlsx'.format(tdy),
            "news" : './data/IEXNews_{}.xlsx'.format(tdy),
            "key" : './data/IEXKeyPerformance_{}.xlsx'.format(tdy)
       }
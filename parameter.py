import datetime

token = *****
ticker ={ 
            "Boeing": "BA",
            "Apple": "aapl",
            "Tesla": "tsla",
            "Alphabet": "goog",
            "Airbnb": "abnb"
        }
tdy = datetime.datetime.now().strftime("%d%b%Y")
path = './data/IEXCloud_{}.xlsx'.format(tdy)
stockdf = []
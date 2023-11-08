import requests
import pyupbit

url = ("https://api.upbit.com/v1/market/all?isFetails=false"
header = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)

tickerList = pyupbit.get_tickers(flat="KRW")
print(tickerList)
coinTickerList = []

for ticker in tickerList:
    coinTickerList.append(ticker[4:])


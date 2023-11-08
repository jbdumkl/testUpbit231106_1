import requests

import pprint
import json
import time

while True:
    url = "https://api.upbit.com/v1/ticker"
    param = {"markets": "KRW-BTC"} #비트코인

    response = requests.get(url, params=param)

    #print(response.text)
    result = response.json()
    #print(result)
    print(result[0]["trade_price"])
    time.sleep(1)


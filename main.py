
#https://github.com/ranaroussi/yfinance
#https://aroussi.com/post/python-yahoo-finance
import yfinance as yf
import pandas as pd
import pprint


#microsoft
#msft = yf.Ticker("MSFT")

ticker = 'msft'
period = '1d'
interval = "1h"


response = yf.download(tickers=ticker,period=period,interval=interval)
#close = data[['Close']]
data = response.to_dict() #working
close = data['Close']
close_values = list(close.values())


first = close_values[0] #testing iteration of first value in close

'''
Managing Multi-Level Columns
How to deal with multi-level column names downloaded with yfinance?
https://stackoverflow.com/questions/63107594/how-to-deal-with-multi-level-column-names-downloaded-with-yfinance/63107801#63107801
'''


def main():

  #pprint.pprint(msft.info)

  #pprint.pprint(data)
  print(close_values)
  #print(type(close_values)) #prints all the closing values dict_values([257.3399963378906, 254.7899932861328, 255.1649932861328, 256.8299865722656, 255.00999450683594, 253.3699951171875, 252.0, 251.99000549316406])
  #print(first)

if __name__ == '__main__':
  main()



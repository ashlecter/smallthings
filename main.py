
#https://github.com/ranaroussi/yfinance
#https://aroussi.com/post/python-yahoo-finance
import yfinance as yf
import pandas as pd
import pprint


#microsoft
#msft = yf.Ticker("MSFT") #prints a bunch of data about the stock we don't need, but keeping this here in case

ticker = 'sg'
period = '1d'
interval = "15m"


response = yf.download(tickers=ticker,period=period,interval=interval)
#close = data[['Close']]
data = response.to_dict() #working
close = data['Close']
close_values = list(close.values())


first = close_values[0] #testing iteration of first value in close


def main():

  #pprint.pprint(msft.info)

  print(close_values) #prints list of close values [257.3399963378906, 254.7899932861328, 255.1649932861328, 256.8299865722656, 255.00999450683594, 253.3699951171875, 252.0, 251.99000549316406]

  #print(first)

if __name__ == '__main__':
  main()



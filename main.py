
#https://github.com/ranaroussi/yfinance
import yfinance as yf
import pprint


#microsoft
msft = yf.Ticker("MSFT")

def main():

  pprint.pprint(msft.info)

if __name__ == '__main__':
  main()



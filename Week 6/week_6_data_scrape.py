
from bs4 import BeautifulSoup
import urllib.request
import json
import csv

def open_file():
    tickers =[]
    with open('ticker.txt','r') as ticker_symbols:
        for item in ticker_symbols:
            tickers.append(item.strip('\n'))
    ticker_symbols.close()
    return tickers
#set URL equal to the term we want to search
def getSearchURL (ticker):
  url ='https://finance.yahoo.com/quote/%s?p=%s' % (str(ticker), str(ticker))
  return url

#open URL and set it to response variable
def getHTMLPageText(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        return response.read()

#loop through set and create a list that can then be output
def create_list(list,ticker):
    info_list = []
    info_list.append(ticker)
    for item in list:
        info_list.append(item.string)
    return info_list

#output selected information to CSV
def output(list):

    with open('stock_info.csv', 'a') as stock_info:
        line_writer = csv.writer(stock_info,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        line_writer.writerow(list)

#create soup object from URL and parse out only code that meets certain attributes
def soup_parser (URL):
    # use BeautifulSoup to open webpage and set equal to soup variable
    soup = BeautifulSoup(URL, 'html.parser')
    # only bring back certain attributes
    # sets all span with a to variable eles
    eles = soup.find_all('span', attrs={'class': 'Trsdu(0.3s)'})
    return eles

def main():
    #open file that contains ticker symbols you want to scrape
    ticker_symbols = open_file()

    #loop through ticker symbols and export information to CSV file
    for symbol in ticker_symbols:
        pageText = getHTMLPageText(getSearchURL(symbol))
        output(create_list(soup_parser(pageText),symbol))



if __name__ == "__main__":
    main()



#print(soup.prettify())

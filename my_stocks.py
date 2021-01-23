"""
Robinhood Trading Assistant
@null-talisman

1. Get current prices of stocks entered in stocks.txt file
2. Compare these current prices against old prices stored in update.txt
    - If a significant change is detected, write the change info to news.txt
        and then:
        - run mail.py to email info from news.txt to specified user. 
    - If no significant change is detected, the current prices will be updated 
      in the update.txt file via a bash script.
"""

# imports 
import os 
import datetime
import robin_stocks as rs
from dotenv import load_dotenv

# user info 
ROBIN_USER = os.getenv("ROBIN_USER")
ROBIN_PASS = os.getenv("ROBIN_PASS")

# global variables
STOCK_NAMES = []
OLD_STOCK_PRICES = []
NEW_STOCK_PRICES = []

# main 
def main(): 
    # login to robinhood with stored creds
    login()
    # get current date and time
    getTime()
    # get stocks to watch
    try:
        getStockNames()
    except:
        pass
    # get current price of each stock
    getStockPrices(STOCK_NAMES)
    # get old price of stock stored in update.txt
    getOldPrices()
    # compare the lists and return % inc/dec
    comparePrices()

# get prices of stocks stored in a list, write to update.txt
def getStockPrices(stocks):
    # for each stock in list of stocks
    for stock in stocks:
        # get latest price for stock
        stock_price=str(rs.stocks.get_latest_price((stock), priceType=None, includeExtendedHours=True))
        stock_price_len = len(str(stock_price))
        print(stock + ": " + "$" + stock_price[2:stock_price_len-6])
        NEW_STOCK_PRICES.append(stock_price[2:stock_price_len-6])

# get old prices from update.txt and append them to old price list
def getOldPrices():
    priceFile = open("update.txt", "r")
    oldPriceInfo = priceFile.read().splitlines()[4:]
    for line in oldPriceInfo:
        # prices are stored as 'TSLA: $845.46' so we need to find '$' and start from there
        index = line.find('$')
        lineLen = len(line)
        oldPrice = line[index+1:lineLen]
        # append this old price to old price list
        OLD_STOCK_PRICES.append(oldPrice)

# we have a list of current prices and old prices. compare them. 
def comparePrices():
    now = datetime.datetime.now()
    sigChange = False
    index = 1
    listLength = len(OLD_STOCK_PRICES)
    # delete old change file
    os.remove("news.txt")
    newNews = open("news.txt", "w+")
    while index < listLength:
        new = float(NEW_STOCK_PRICES[index])
        old = float(OLD_STOCK_PRICES[index])
        name = STOCK_NAMES[index]
        change = 100 - (new / old * 100)
        prcntChange = float(format(change, '.2f'))
        if (prcntChange > 5.0) or (prcntChange < -5.0):
            sigChange = True
            newNews.write("Significant change detected at " + now.strftime('%H:%M:%S') + "\nStock: " + str(name) + "\nCurrent Price: " + str(new) + "\nOld Price: " + str(old) + "\nChange: %" + str(prcntChange) + "\n")
            # significant change in price detected, send an email with news.txt to user
        index+=1

# login() function for robinhood login
def login():
    # login to robinhood
    rs.login(username=ROBIN_USER, 
             password=ROBIN_PASS, 
             expiresIn=86400, 
             by_sms=True)

# get current date and time
def getTime():
    now = datetime.datetime.now()
    print("******************")
    print("DATE: " + now.strftime('%m-%d-%Y'))
    print("TIME: " + now.strftime('%H:%M:%S'))
    print("******************")

# read in stocks from stocks.txt
def getStockNames():
    StockFile = open("stocks.txt", "r")
    StockInfo = StockFile.read().splitlines()[1:]
    for line in StockInfo:
        # append stock to list
        STOCK_NAMES.append(line)
       
    
### The following code block can be enabled to test a singular symbol
#def testSingleStock():
    # get stock information 
    # aapl_info=rs.stocks.find_instrument_data('AAPL')
    # aapl_price=rs.stocks.get_latest_price('AAPL', priceType=None, includeExtendedHours=True)
    # aapl_quotes=rs.stocks.get_quotes('AAPL')
    # print info back
    # print('***Current Price of \'AAPL\'***')
    # print(aapl_price)


# main runner 
if __name__ == "__main__":
    main()

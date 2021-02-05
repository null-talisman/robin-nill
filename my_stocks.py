"""
Robinhood Trading Assistant (Python 3.6.9)
@null-talisman

For Windows Users (Method #1):
    1. Install WSL (Windows Subsystem for Linux): https://docs.microsoft.com/en-us/windows/wsl/install-win10
    2. Get Windows Terminal for easier access to WSL: https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab
    3. Open up Windows Terminal:
        - On the toolbar, hover over the down-arrow. It should say "Open a new tab." Click and select Ubuntu.
        - Install Python3: sudo apt-get python3
        - Install dotenv package: pip3 install python-dotenv
        - Install robin stocks package: pip3 install robin-stocks
    4. Clone the Github repo from https://github.com/null-talisman/robin-nill
        - git clone https://github.com/null-talisman/robin-nill.git
        - cd robin-nill
    5. Modify the email fields in my_stocks.py:
        - nano my_stocks.py
        - sender_email="test@gmail.com"
        - receiver_email="me@gmail.com"
        - password="Password123!" *for sender email
        - To save and exit, hit CTRL+X and then y
    6. Enter your stock symbols in the stocks.txt file.
        - nano stocks.txt
        - To save and exit, hit CTRL+X and then y
    7. Add your Robinhood credentials to the .env file:
        - nano .env
        - ROBIN_USER="lone_druid@yahoo.com"
        - ROBIN_PASS="Password123!"
        - To save and exit, hit CTRL+X and then y
    8. Modify script path in prog.sh:
        - get current location: pwd
        - nano prog.sh
        - main_file=/home/tyler/robinhood/my_stocks.py -> main-file=[result of pwd]/my_stocks.py
        - To save and exit, hit CTRL+X and then y
    9. $$$

With the default cron configuration, this program is scheduled to run every minute 30 (ex. 4:30, 5:00, 5:30 etc). You can modify 
the cron_cfg.txt to change how often this program runs. Refer to documentation online for configuring cron. You can also modify what 
the program considers a significant change (default is 5%). Modifiable fields will be obvious. Yes, I will make this much easier :)
"""

# imports 
import os 
import datetime
import smtplib
import getpass
import ssl 
import robin_stocks as rs
from dotenv import load_dotenv
from robin_stocks import stocks

# user info 
ROBIN_USER = os.getenv("ROBIN_USER")
ROBIN_PASS = os.getenv("ROBIN_PASS")

# global variables
STOCK_NAMES = []
OLD_STOCK_PRICES = []
NEW_STOCK_PRICES = []
SIG_CHANGE = False
SCAN_TIME = 0

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
    # update
    update()
    print("\n")
    # send email alert
    if SIG_CHANGE == True:
        sendEmail()

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
    priceFile = open("data/update.txt", "r")
    oldPriceInfo = priceFile.read().splitlines()
    for line in oldPriceInfo:
        # prices are stored as 'TSLA: $845.46' so we need to find '$' and start from there
        index = line.find('$')
        lineLen = len(line)
        oldPrice = line[index+1:lineLen]
        # append this old price to old price list
        OLD_STOCK_PRICES.append(oldPrice)

# we have a list of current prices and old prices. compare them. 
def comparePrices():
    global SIG_CHANGE
    now = datetime.datetime.now()
    index = 0
    listLength = len(OLD_STOCK_PRICES)
    # update old change file
    newsFilePath = "data/news.txt"
    newNews = open(newsFilePath, "w+")
    stuff = ""
    while index < listLength:
        #drop = new < old
        new = float(NEW_STOCK_PRICES[index])
        old = float(OLD_STOCK_PRICES[index])
        drop = new < old
        name = STOCK_NAMES[index]
        change = 100 - (new / old * 100)
        prcntChange = float(format(change, '.2f'))
        ############################################################################################################################
        ################################### MODIFY SIGNIFICANT CHANGE VALUE HERE ###################################################
        ############################################################################################################################
        if (prcntChange > 5.0) or (prcntChange < -5.0):
        ############################################################################################################################
            if drop:
                SIG_CHANGE = True
                stuff = stuff + "*SIG CHANGE DETECTED*\n" + "Significant change detected at " + now.strftime('%H:%M:%S') + "\nStock: " + str(name) + "\nCurrent Price: " + str(new) + "\nOld Price: " + str(old) + "\nChange: %-" + str(prcntChange) + "\n\n"
            if not drop:
                prcntChange = abs(prcntChange)  
                SIG_CHANGE = True
                stuff = stuff + "*SIG CHANGE DETECTED*\n" + "Significant change detected at " + now.strftime('%H:%M:%S') + "\nStock: " + str(name) + "\nCurrent Price: " + str(new) + "\nOld Price: " + str(old) + "\nChange: %" + str(prcntChange) + "\n\n"
        index+=1
    newNews.write(stuff)

# login() function for robinhood login
def login():
    # login to robinhood
    rs.login(username=ROBIN_USER, 
             password=ROBIN_PASS, 
             expiresIn=604800, 
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
    StockFile = open("data/stocks.txt", "r")
    StockInfo = StockFile.read().splitlines()[1:]
    for line in StockInfo:
        # append stock to list
        STOCK_NAMES.append(line)

# update stock update file
def update():
    updateFile = open("data/update.txt", "w+")
    for i in range(len(NEW_STOCK_PRICES)):
        updateFile.write(STOCK_NAMES[i] + ": $" + NEW_STOCK_PRICES[i] + "\n")

# sendEmail function 
def sendEmail():   
    # using .starttls()
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    # enter desired email info
    sender_email = "youremail@gmail.com"
    receiver_email = "youremail@gmail.com"
    password = "Password123!"
    # password = getpass.getpass(prompt='Password: ', stream=None)

    # get updated info
    info_file = open("data/update.txt", "r")
    change_file = open("data/news.txt", "r")
    update_info = info_file.read().splitlines()
    change_info = change_file.read().splitlines()
    # update info for email
    final_update_info = "*CURRENT PRICES*\n"
    final_change_info = ""
    for line in change_info:
        final_change_info = final_change_info + str(line) + "\n"
    for line in update_info:
        final_update_info = final_update_info + str(line) + "\n"
    print(final_change_info)
    print(final_update_info)


    # message ?
    now = datetime.datetime.now()
    SCAN_TIME = now.strftime('%m-%d %H:%M')
    #SCAN_DATE = datetime.datetime.today()
    message = """\
    Robinhood Update %s
    

    %s \n %s        .""" % (SCAN_TIME, final_change_info, final_update_info)


    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 


# main runner 
if __name__ == "__main__":
    main()

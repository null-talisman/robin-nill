# using robin stocks for robinhood 
# null-talisman 

# imports 
import robin_stocks as rs 
import os 

# user info 
robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

# main 
def main(): 

    # login to robinhood
    rs.login(username=robin_user, 
             password=robin_pass, 
             expiresIn=86400, 
             by_sms=True)

    # get current info of my stocks
    stock_list=['TMUS','BILI','KODK','MSFT','AAPL']
    for stock in stock_list:
        #stock_info=str(rs.stocks.find_instrument_data(stock))
        stock_price=str(rs.stocks.get_latest_price((stock), priceType=None, includeExtendedHours=True))
        stock_quotes=str(rs.stocks.get_quotes(stock))
        stock_price_len = len(str(stock_price))
        print(stock + ": " + "$" + stock_price[2:stock_price_len-6])

    ### The following code block can be enabled to test a singular symbol
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

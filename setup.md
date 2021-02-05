# Robinhood Trading Assistant (Python 3.6.9)
@null-talisman
youngnilla@yahoo.com
    
# For Windows Users (Method #1): 
    1. Open up your start menu, type in "cmd" and hit enter.
    2. In your command prompt terminal, type in "python3" and hit enter. 
        2a. If you have Python 3 already installed, it will bring you to the Python shell. 
        2b. If you don't have Python3 installed, it should open up the Windows Store page. Install it. 
    3. In your command prompt terminal, type the following commands:
        3a. ""pip3 install python-dotenv""
        3b. ""pip3 install robin-stocks""
    4. Go to https://github.com/null-talisman/robin-nill. Click on the "code" button and click "Download ZIP". 
        4a. If you don't have WinRar, I strongly suggest downloading it. Otherwise simply open and extract the robinhood folder to your Documents.
    5. Using Notepad, modify the email fields in my_stocks.py:
        - sender_email="test@gmail.com"
        - receiver_email="me@gmail.com"
        - password="Password123!" *for sender email
    6. Using Notepad, enter your stock symbols in the stocks.txt file.
    7. Using Notepad, add your Robinhood credentials to the .env file:
        - ROBIN_USER="lone_druid@yahoo.com"
        - ROBIN_PASS="Password123!"
    8. Open up your start menu, type in "task scheduler' and hit enter.
        8a. Click "Create Task..."
        8b. Name it. Make sure it is configured for your correct OS. 
        8c. Go to "Triggers" tab. Click "New...". Under settings, select "Daily" and under Advanced settings, select "Repeat task every: 30 minutes for a duration of indefinitely" Set your start time to the nearest hour/half-hour. 
        8d. Go to "Actions" tab, click "New...", click "Browse..." and navigate to the robinhood folder you extracted earlier to your Documents. Select the my_stocks.py file.
        8e. Click "OK"
    9. $$$

# Notes 
With the default cron configuration, this program is scheduled to run every minute 30 (ex. 4:30, 5:00, 5:30 etc). You can modify 
the cron_cfg.txt to change how often this program runs. Refer to documentation online for configuring cron. You can also modify what 
the program considers a significant change (default is 5%). Modifiable fields will be obvious. Yes, I will make this much easier :)

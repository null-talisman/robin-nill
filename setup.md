# Robinhood Trading Assistant (Python 3.6.9)
@null-talisman
youngnilla@yahoo.com

# For Windows Users (Method #1):
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

# Notes 
With the default cron configuration, this program is scheduled to run every minute 30 (ex. 4:30, 5:00, 5:30 etc). You can modify 
the cron_cfg.txt to change how often this program runs. Refer to documentation online for configuring cron. You can also modify what 
the program considers a significant change (default is 5%). Modifiable fields will be obvious. Yes, I will make this much easier :)
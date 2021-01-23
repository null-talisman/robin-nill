# Nilla's Robinhood Work

This repository contains a set of resources needed for Robinhood email updates of your portfolio.

# v0.1 notes
It is currently set up with static values for stocks, but I will change this soon. The set of tools 
used for this feature are:
  - my_stocks.py which uses Robin Stocks API to get stock updates from Robinhood
  - mail.py which sends an email to the user
  - update.txt contains the information gathered from my_stocks.py
  - prog.sh is a shell script that runs these python programs
  
I have a cron job running prog.sh M-F at 9AM and 5PM. 

# v0.2 notes
Alright, made some modifications to this project this morning. Quite a few notes:
  - Modulized the code for easier readability and troubleshooting. 
  - Stock names are now entered in the stocks.txt file and read in. 
  - Robinhood user credentials are now stored in a .env file and read into my_stocks.py.
  - Removed the password for test Gmail account I had in here (youngnillatest@gmail.com).
  - Old prices are pulled from update.txt and compared against current prices when my_stocks.py runs. 
  - If a significant change is detected (>= or <= 5% at the moment) then a note will be written to news.txt. For example (fake numbers): 
    Significant change detected
    Stock: NFLX
    Current Price: 576.0
    Old Price: 371.15
    Change: %-55.19
  - After my_stocks.py checks for major change, it will send out an email if detected (in-progree) or simply update the prices in update.txt
  - Update2.txt is useless. Ignore it. Mail-2 is useless too. They'll be removed. 
  - I *have not* made changes to mail.py, prog.sh, or cron_cfg.txt. These files are essentially: 
      mail.py - python program for sending the email to specified email address
      prog.sh - shell script for running these python programs from linux CLI and managing files. 
      cron_cfg.txt - configuration settings for crons scheduler. this can be modifed by the user to modify the interval in which this tool runs. cron will essentially 
                run the prog.sh script and run these python files in a logical order. (In-progree)
        
 # On the Horizon
 1. Verify email messages when a signicant change is detected. 
 2. Iron out issues with cron job (I'm not sure if me using WSL is impacting this).
 3. Clean up comments. There are A TON of comments used for debugging. 
 4. Directory restructure. It's kind of a mess right now. 
 5. The authentication to your robinhood account expires after 24 hours (I think). So I'd like
    to modify these to be longer.
 5. As of right now, utilizing this tool takes a little bit of work. I will eventually create some sort of documentation to help with the setup process and automate as much of that process as possible. In a perfect world, once complete, I'll publish this as a package to PyPI :) 



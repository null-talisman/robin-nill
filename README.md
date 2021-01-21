# Nilla's Robinhood Work

This repository contains a set of resources needed for Robinhood email updates of your portfolio.
It is currently set up with static values for stocks, but I will change this soon. The set of tools 
used for this feature are:
  - my_stocks.py which uses Robin Stocks API to get stock updates from Robinhood
  - mail.py which sends an email to the user
  - update.txt contains the information gathered from my_stocks.py
  - prog.sh is a shell script that runs these python programs
  
I have a cron job running prog.sh M-F at 9AM and 5PM. 


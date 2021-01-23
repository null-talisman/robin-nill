#! /bin/bash

# bash script to run Robinhood updates.
# file locations 
update_file=/home/tyler/robinhood/update.txt
main_file=/home/tyler/robinhood/my_stocks.py
# run my_stocks.py
python3 $main_file
# probably amateur-hour right here
rm -r $update_file
touch $update_file
chmod 777 $update_file
# re-run my_stocks.py and update update.txt
python3 $main_file > $update_file



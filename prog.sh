#! /bin/bash

# bash script to run Robinhood updates
# 1 - update update.txt
update_file=/home/tyler/robinhood/update.txt
rm $update_file
# touch $update_file
# chmod 666 $update_file
# 2 - run my_stocks.py
python3 my_stocks.py > update.txt
# 3 - run mail.py 
python3 mail.py



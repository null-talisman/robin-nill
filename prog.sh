#! /bin/bash

# bash script to run Robinhood updates
# 1 - update update.txt
update_file=/home/tyler/robinhood/update.txt
if [ -f $update_file ]
   then 	
      rm $update_file
      touch $update_file
      chmod 666 $update_file
fi
# 2 - run my_stocks.py
python3 /home/tyler/robinhood/my_stocks.py > update.txt
# 3 - run mail.py 
# python3 /home/tyler/robinhood/mail.py

# return update.txt content
cat update.txt



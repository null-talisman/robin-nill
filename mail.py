# send email ?
# @null-talisman

# imports
import datetime
import smtplib
import getpass
import ssl 

# using .starttls()
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "youngnillatest@gmail.com"
receiver_email = "youngnillatest@gmail.com"
password = "Yahoo850!"
# password = getpass.getpass(prompt='Password: ', stream=None)

# get updated info
info_file = open("update.txt", "r")
update_info = info_file.read().splitlines()

# message ?
now = datetime.datetime.now()
time_info = now.strftime('%m-%d %H:%M')
message = """\
Subject: Robinhood Update %s
 

%s        .""" % (time_info, update_info)


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

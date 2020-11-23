# send email ?
# @null-talisman

# imports
import smtplib
import ssl 

# using .starttls()
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "youngnillatest@gmail.com"
password = input("Type your password and press enter: ")

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
except Exception as e:
        # Print any error messages to stdout
        print(e)
finally:
        server.quit() 

# SSL 
# port = 465
# password = input("Password: ") 

# Create a secure SSL context
# context = ssl.create_defaut.context()
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#         server.login("youngnillatest@gmail.com", password)
#             # TODO: Send email here

# Python program for sending email
# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "sender mail"
# Receivers email
rec_email = "receiver model"

message = "Contianer stop working reluanching it."
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("sender mail", "sender pass")
print("Login Success!")
# Send Email
server.sendmail("reciever name", "sneder name", message)
print(f"Email has been sent successfully to {rec_email}")

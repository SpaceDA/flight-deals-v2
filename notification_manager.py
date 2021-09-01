#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib
import os



TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = os.environ['TWILIO_VIRTUAL_NUMBER']
TWILIO_VERIFIED_NUMBER = os.environ['TWILIO_VERIFIED_NUMBER']

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_alert(self, message):
        message = self.client.messages.create(
            body=message,
            from_= TWILIO_VIRTUAL_NUMBER,
            to= TWILIO_VERIFIED_NUMBER
        )
        print(message.status)
    def send_email(self, message, to_addrs):

        from_addr = os.environ['from_addr']
        pw = os.environ['gmail_pw']
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=from_addr, password=pw)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=message)
        connection.close()


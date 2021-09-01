#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib



TWILIO_SID = SID
TWILIO_AUTH_TOKEN = TOK
TWILIO_VIRTUAL_NUMBER = NUM
TWILIO_VERIFIED_NUMBER = NUM

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

        from_addr = from
        pw = p2
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=from_addr, password=pw)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=message)
        connection.close()


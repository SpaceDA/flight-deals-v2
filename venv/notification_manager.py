#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib



TWILIO_SID = "ACad2fdecff6acd31041108876dd7be896"
TWILIO_AUTH_TOKEN = "4666cb83b7d60ec5a859588ac928a3d8"
TWILIO_VIRTUAL_NUMBER = "+18647218551"
TWILIO_VERIFIED_NUMBER = "+16317963616"

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

        from_addr = "florida.man1775@gmail.com"
        pw = "marines1775!"
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=from_addr, password=pw)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=message)
        connection.close()


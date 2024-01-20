import smtplib
from twilio.rest import Client
import os
from decouple import config

TWILIO_SID = config("TWILIO_SID")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = config("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = config("TWILIO_VERIFIED_NUMBER")
MAIL_PROVIDER_SMTP_ADDRESS = config("MAIL_PROVIDER_SMTP_ADDRESS")
MY_EMAIL = config("MY_EMAIL")
MY_PASSWORD = config("MY_PASSWORD")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
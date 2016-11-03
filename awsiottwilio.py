import config
import time
from twilio.rest import TwilioRestClient

client = TwilioRestClient(config.account_sid, config.auth_token)

def one_sms():
    client.messages.create(body="!", to=config.notify_number, from_=config.twilio_number)

def five_sms():
    for i in range(5):
        client.messages.create(body="!", to=config.notify_number, from_=config.twilio_number)
        time.sleep(5)

def call():
    client.calls.create(to=config.notify_number, from_=config.twilio_number,
                        url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")




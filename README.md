# awsiottwilio
A simple app that uses AWS Lambda and the [twilio-python library](https://github.com/twilio/twilio-python) to connects an AWS IoT button to Twilio. 

The IoT button can be used to trigger events in Twilio such as sending texts and making phone calls. 

The current configuration is set to send one sms message, five sms messages, and make a phone call on an IoT Button, single click, double click, and long click respectively. 


###Config file

```
# config.py
account_sid = "Your Twilio account SID"
auth_token = "Your Twilio auth token"
notify_number = "+The number that you want to send calls or texts to"
twilio_number = "Your Twilio phone number"
```


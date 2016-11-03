import awsiottwilio

def lambda_handler(event, context):
    dict = event
    click = dict.get('clickType')
    if click == "SINGLE":
        awsiottwilio.one_sms()
    if click == "DOUBLE":
        awsiottwilio.five_sms()
    if click == "LONG":
        awsiottwilio.call()


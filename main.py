from twilio.rest import Client

account_sid = "Your account SID here"
auth_token = "[Your auth token here]"
client = client(account_sid, auth_token)


message = client.messages.create(
    from = "Your Twilio phone number here",
    body = "Write down your message here"
    to = "Write the recievers phone number here"
)


print(message.sid)

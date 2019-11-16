from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACde1b2cae6c069719a0b93f980623cddc'
auth_token = 'ac5a3921290d2ca1b0215ba73c56586a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello! What can I help you with?",
                     from_='+12055574327',
                     to='+16266882932'
                 )

print(message.sid)


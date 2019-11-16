from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    # Add a message
    if body == "hello":
        resp.message("Hi! How can I help? \n (1) Riot \n (2) Animals \n (3) Grafiti")

    
    # jmak is stupid




    return str(resp)







if __name__ == "__main__":
    app.run(debug=True)

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
        resp.message("Hi! This is Citizen help. \n If there is an issue, reply: HELP"
    if body == "HELP":
        resp.message("What is the issue? \n (1) Riot \n (2) Animals \n (3) Grafiti \n (4) Noise Complaint")
    else:
        resp.message("Have a good day!")

    

    return str(resp)




if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, request, redirect, session 
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    saved = session.get("saved", 0)
    # Determine the right reply for this message
  
    Environmental_Wildlife = {'Abandoned Animal':['MSPCA - Animal Cruelty','8006285808'] , 'Flooding':['Boston Water and Flooding','6176353850'], 'Air/Water Pollution':['National Response Center','18004248802'],'Pest Control':['Security Pest Control','6172649898']}
    Maintanence_Housing = {'Dangling Electricity Cables':['National Grid Massachusetts','18004651212'],'Fire Hydrant':['Boston City Hall','6176354000'],'Public Transportation Accident':['Boston Transportation Department','6173434570'],'Slippery Streets':['Vision Zero','6176351347'],'Broken Traffic/Street Lights':['National Grid Massachusetts','18003223223'],'Natural Gas Leak':['National Grid Massachusetts','18002335325'],'Sewage Issue':['Boston Water and Sewer Commission','6179897000'],'Power Outage':['National Grid','8004651212'],'Traffic Management':['Transportation Boston Government','6176353900']}
    People_Human_Services = {'Riot Protest':['Boston Police Department','6173434633'],'Noise':['City of Boston','6176353850'],'Transients':['Boston Public Health Commission - Homeless services','6175342526'],'Drug Activity':['Boston Police Department','6173434633'],'Drug Addiction':['Boston ASAP Counseling','6174825292'],'Public Nudity':['Bos 311','311'],'Underage Drinking':['Boston Police Department','6176350029'],'Suspected Child Abuse':['Department of Children and Families','6177482000'],'Suspected Abuse':['Nationwide Safelink','8777852020'],'Racism':['Resilence and Racial Equality','6176350029'],'Political Dishonesty':['City Boston','6176358683'],'Drunk Driving':['Boston Police Department','911'],'Robbery':['Boston Police Department','911'],'Lost Person':['National Center for Lost Missing and Exploited','8008435678']}
    Trash_Blockage_Vandelism = {'Illegal Parking':['City of Boston','311'],'Graffiti':['Property Management','6176354100'],'Trash on Streets':['Public Works','6176354900'],'Road Kill':['Boston 311','311'],'Blockage on Roadways':['Boston Transportation Department','617 3434570']}
    print(body)
    if body == "hello":
        resp.message("Hi! This is Citizen help. \n If there is an issue, reply: boston")
        return str(resp)
    elif body == "boston":
        resp.message("What is the issue? \n (1) Environmental_Housing \n (2) Maintenance_Housing \n (3) People_Human_Services \n (4) Trash_Blockage_Vandalism")
        return str(resp)
    
    # Code for body 1 --> copy this format for the rest of the code and you should be fine
    elif body == "1":
        res_message = ""
        for key in Environmental_Wildlife.keys():
            res_message += str(key) + "\n "
        resp.message(res_message + "\nPlease type in the category.")
        return str(resp)
    elif body in Environmental_Wildlife:
        resp.message("Please contact " + Environmental_Wildlife[body][0] + " at " + Environmental_Wildlife[body][1])
        return str(resp)
    #############################################    
    elif body == "2":
        res_message = ""
        for key in Maintanence_Housing.keys():
            res_message += str(key) + "\n "
        resp.message(res_message + "\nPlease type in the category.")
        return str(resp)
    elif body in Maintanence_Housing:
        resp.message("Please contact " + Maintanence_Housing[body][0] + " at " + Maintanence_Housing[body][1])
        return str(resp)
    elif body == "3":
        res_message = ""
        for key in People_Human_Services.keys():
            res_message += str(key) + "\n "
        resp.message(res_message + "\nPlease type in the category.")
        return str(resp)
    elif body in People_Human_Services:
        resp.message("Please contact " + People_Human_Services[body][0] + " at " + People_Human_Services[body][1])
        return str(resp)
    elif body == "4":
        res_message = ""
        for key in Trash_Blockage_Vandelism.keys():
            res_message += str(key) + "\n "
        resp.message(res_message + "\nPlease type in the category.")
        return str(resp)
    elif body in Trash_Blockage_Vandelism:
        resp.message("Please contact " + Trash_Blockage_Vandelism[body][0] + " at " + Trash_Blockage_Vandelism[body][1])
        return str(resp)
    elif body.isdigit():
        resp.message("Sorry, we do not have an answer for this. Please choose a valid category.")
        return str(resp)
    else:
        resp.message("Thank you for using Citizen Help. Have a nice day!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



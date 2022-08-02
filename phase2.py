import os, sys
from flask import Flask ,request 
import json
from pymessenger import Bot
from pprint import pprint
from utils2 import generate_user_response

VERIFICATION_TOKEN ="hello"
PAGE_ACCESS_TOKEN="EAADURjqMIXIBADCkBAizd2kjOAOlyayZAcyhu1I9urHYyZABdCBpIpG0EGCuGiGed67bX8j0gVwoKo1UJug0jA6eZBag4NAthiscPziz95hZBtsG3dMQZAgTOZCCnEzcZAGWY8ro52c0cvTkz4cQZCQVxAaBr5ZBKUwbS7lAxmTWZAlwZDZD"
app=Flask(__name__)
bot=Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET']) #lma ygli access a3ml call function
def verify():
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")==VERIFICATION_TOKEN:
            return "verification token mismatch",403
        return request.args["hub.challenge"],200
    return "Hello-world",200


@app.route('/', methods=['POST'])
def webhook():
    #printmsg("I am here")
    data=request.get_json()
    printmsg(data)
    #printmsg(request.data)
    process_data(data)
    return "ok",200

  
def process_data(data):
    if data ["object"]=="page":  #if true hngeeb entry [list]
        for entry in data ["entry"]:
            for messaging_event in entry ["messaging"]: #3shan ad5ol 3la list 
                sender_id = messaging_event["sender"]["id"]
                recipient_id = messaging_event["recipient"]["id"] #bgeb mn eldict elrecipient key
                if messaging_event.get("message"):
                     if "text" in messaging_event["message"]: #key:text 
                          messaging_text = messaging_event["message"]["text"] # message text ="hello there"
                     else:
                          messaging_text="no text" # lw mfesh text 
                     printmsg(messaging_text)
                     #response= messaging_text
                     response= generate_user_response(messaging_text)
                     bot.send_text_message(sender_id,response)
                   

def printmsg(msg):
    pprint (msg)
    sys.stdout.flush()

if __name__=="__main__":
    app.run(debug=True,port=80)
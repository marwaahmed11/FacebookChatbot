
from pprint import pprint


def generate_user_response (message_text):
    response=None
    sent=message_text
   
    if sent=="hello":
        response="Hello,how are you."
    elif sent=="hi":
         response="Hi,how are you."     
    elif sent=='what are available colours of mom fit jeans?':
        response="Black - White - Dark blue "
    elif sent=='what are available colours of wide leg jeans?':
        response="Black - White - Dark blue "
    elif sent=='what are available colours of skinny jeans?':
        response="Black - White - Dark blue "
    elif sent=='what are available colours of boyfriend jeans?':
        response="Black - White - Dark blue "      
    elif sent=='what is available size of skinny jeans?':
        response="32-34-36-38"
    elif sent=='what is available size of mom fit jeans?':
        response="32-34-36-38"
    elif sent=='what is available size of wid leg jeans?':
        response="32-34-36-38"
    elif sent=='what is available size of boyfriend jeans?':
        response="32-36-38-40" 
    elif sent=='what is price of skinny jeans?':
        response="starting from 500 LE"
    elif sent=='what is price of wid leg jeans?':
        response="starting from 400 LE"
    elif sent=='what is price of boyfriend jeans?':
        response="starting from 500 LE"
    elif sent=='what is price of mom fit jeans?':
        response="starting from 450 LE"     
    elif sent=='How much does delivery cost?':
        response="cairo 30LE - Alex 50LE -Luxor 70LE"      
    elif sent=='what is location of your branches?':
        response="Sorry,it is only online store"   
    else:
        response="Sorry, I didn't understand your message!"
    return response
        
        

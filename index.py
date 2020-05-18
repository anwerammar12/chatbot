import os 
import requests
import traceback
import json
from flask import Flask, request

token='EAAQhYHRp03UBAIAodUOat0ssleYqE9jhPEXgY9YNuqaKcxr9vqmmXZCHo45asn95xGCnWiNCeqIKxZA20Nzt5ybwtH3ocoQ9Aw981ZBhZCCDTGddQ0zRH9GtDoqOU8bk83D2hNgdx1ZB9KLB90nrglbMqegfNR2JyGmkZCbonGGwZDZD'
app=Flask(__name__)

def send_message(sender):
	return {
		'recipient': {'id':sender},
		'message':{'text':'chbik khra'}
			}



def location_quick_reply(sender):
    return {
        "recipient": {
            "id": sender
        },
        "message": {
            "text": "Share your location:",
            "quick_replies": [
                {
                    "content_type": "location",
                }
            ]
        }
    }



@app.route('/',methods=['GET','POST'])
def webhook():
	if request.method=='POST':
		try:
			print('\nRECEPTION\n')
			data=json.loads(request.data.decode())
			text=data['entry'][0]['messaging'][0]['message']['text']
			print(text)
			sender=data['entry'][0]['messaging'][0]['sender']['id']
			payload=location_quick_reply(sender)
			r = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token='+token, json=payload)
			with open('error.txt','w') as f:
				f.write(str(r.text))
			print(r.text)
		except Exception as e:
			print(traceback.format_exc())

	elif request.method=='GET':
		if request.args.get('hub.verify_token')=='hello':
			return request.args.get('hub.challenge')
		return 'Wrong Verify Token'
	return 'Nothing'

if __name__=='__main__':
	app.run(debug=True)
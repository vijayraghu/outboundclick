#!/usr/bin/env python

import os
import twilio.twiml
from twilio.rest import TwilioRestClient
from flask import Flask
from flask import request

# Flask app should start in global layout
app = Flask(__name__)

client =  TwilioRestClient(os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))

# Entry to outbound from pythontwil
@app.route('/outbound', methods=['POST'])
def outbound():
  response = twiml.Response()
  response.say("Please hold on while we connect you to an agent")
  with response.dial() as dial:
    dial.number(os.environ.get('DNIS_NUMBER'))
  return str(response)
			
if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=False, port=port, host='0.0.0.0')

from flask import Flask
from flask_restful import request
from urllib import parse
import chatbot as cb
import json
import logging 

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

app = Flask(__name__)

@app.route('/chatbot')
def Chatbot():
    okay = True

    sentence = request.args.get('sentence')
    if sentence and sentence != "":
        bot_response = str(cb.chatbot.get_response(sentence))
    else:
        okay = False
        bot_response = ""
    data = { 'answer' : bot_response, 'okay' : okay, 'question' : sentence }

    return json.dumps(data)
 

if __name__ == '__main__':
    app.run(host='0.0.0.0')
from flask import Flask, make_response
from flask_restful import request, Resource, Api
from json import dumps
import urllib
import chatbot as cb


app = Flask(__name__)
api = Api(app)


# Chatbot Class
class Chatbot(Resource):
    # GET 메소드
    def get(self):
        okay = True
        sentence = request.args.get('sentence', '')
        
        if sentence and sentence != "":
            bot_response = str(cb.chatbot.get_response(sentence))
        
        else:       # 문자열이 없을경우, ''의 경우도 해당
            okay = False
            bot_response = ""
            
        # bot_response - 챗봇 대답
        # okay - 성공적으로 챗봇이 작동하였는지 유무, 링크가 정상적인지 체크
        # question - 사용자의 질문
        data = { 'answer' : bot_response, 'okay' : okay, 'question' : sentence }
        dump_data = dumps(data, ensure_ascii=False, indent=4)

        return make_response(dump_data)
 

api.add_resource(Chatbot, '/chatbot')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
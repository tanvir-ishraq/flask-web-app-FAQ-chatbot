
#make sure credentials.yml and endpoint.yml have nevessary code
## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

import requests

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": userText})

    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}") #testing
        return str(bot_message)
    
    #return chatbot_response(userText)


# rasa run -m models --enable-api --cors "*" # -vv for debug

if __name__ == '__main__':    
    app.run(debug=True, host="192.168.1.180",port="5004", ssl_context=("./rasacert.pem", "./rasakey.key")) 
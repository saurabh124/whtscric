from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup
import urllib.request
score_page = r'http://static.cricinfo.com/rss/livescores.xml'
page = urllib.request.urlopen(score_page)
soup = BeautifulSoup(page, 'html.parser')
result = soup.find_all('description')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    i = 0
    for match in result :
       i=i+1
       a = match.get_text()
       print(a)
       if i == 2:
         break
    msg = request.form.get('Body')
    
    if msg =='Cricket':
        resp = MessagingResponse()
        resp.message("{}".format(a))

        return str(resp)
    else:
        resp = MessagingResponse()
        resp.message("enter valid input i.e Cricket")
        return str(resp)
if __name__ == "__main__":
    app.run(debug=True)

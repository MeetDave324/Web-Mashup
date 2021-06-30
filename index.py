from flask import Flask,request,render_template
import pickle
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("/index.html")

@app.route('/search',methods=['POST','GET'])
def login(): 
    
    inp=request.form['word']   
    print(inp)
    authenticator = IAMAuthenticator('EtYKFV6o4oYqhJ8RU_gMwBzw_a0Ax3k7iR0KAng5T4HQ')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/9b5e188b-8981-4c9b-bb97-62d8a5d596ea')
     
    BASE_LANGUAGE = 'en'
    language = language_translator.identify(inp).get_result()
    source_a=language['languages'][0]['language']
    print(source_a)
    response = language_translator.translate(
                inp,
                source=source_a,
                target='en')
    res = response.get_result()
    print(res)
    text = res['translations'][0]['translation']
    print(text)
    trans_text=text
    url="http://localhost:105/wiki/"
    params= {'word':text}
    r=requests.get(url= url,params=params)
    data=r.json()
    #print(data)
    summary=data['summary']
    #print(summary)
    response = language_translator.translate(
                summary,
                source='en',
                target=source_a)
    res = response.get_result()
    #print(res)
    text = res['translations'][0]['translation']
    print(text)
    return render_template('index.html',info=text,text=trans_text)

if __name__ == '__main__':
    app.run()
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:58:32 2020

@author: meet
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests
authenticator = IAMAuthenticator('EtYKFV6o4oYqhJ8RU_gMwBzw_a0Ax3k7iR0KAng5T4HQ')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/9b5e188b-8981-4c9b-bb97-62d8a5d596ea')

BASE_LANGUAGE = 'en'
print('Enter the Word')
inp=input()
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

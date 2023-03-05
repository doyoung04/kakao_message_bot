import requests
import json

params = {
    'REST_API_key': 'key',
    'Redirect_URI': 'https://example.com/oauth',
    'code': 'code'
}

url = 'https://kauth.kakao.com/oauth/token'
client_id = params['REST_API_key']
redirect_uri = params['Redirect_URI']
code = params['code']

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data)
tokens = response.json()

access_token = tokens['access_token']

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data = {
       'object_type': 'text',
       'text': '테스트입니다',
       'link': {
           'web_url': 'https://developers.kakao.com',
           'mobile_web_url': 'https://developers.kakao.com'
       },
       'button_title': '키워드'
   }
   
data = {'template_object': json.dumps(data)}
response = requests.post(url, headers=headers, data=data)
response.status_code

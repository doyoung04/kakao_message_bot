import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up driver
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

# Set up OAuth parameters
REST_API_key = 'key'
Redirect_URI = 'https://example.com/oauth'
url = f'https://kauth.kakao.com/oauth/authorize?client_id=\
{REST_API_key}&redirect_uri={Redirect_URI}&response_type=code'

# Navigate to OAuth page and log in
driver.get(url)
driver.find_element(By.NAME, 'loginKey').send_keys('id_kakao')
driver.find_element(By.NAME, 'password').send_keys('pw_kakao')
driver.find_element(By.CSS_SELECTOR, 'button.submit').click()

# Wait for page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h1'), 'Example Domain'))

# Get access token
url = 'https://kauth.kakao.com/oauth/token'
client_id = REST_API_key
redirect_uri = 'https://example.com/oauth'
code = driver.current_url[31:]

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
}

response = requests.post(url, data=data)
tokens = response.json()

access_token = tokens['access_token']

# Send message
url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + access_token
}

data = {
    'object_type': 'text',
    'text': '보낼 메시지를 입력하세요',
    'link': {
        'web_url': 'https://developers.kakao.com',
        'mobile_web_url': 'https://developers.kakao.com'
    },
    'button_title': '키워드'
}

data = {'template_object': json.dumps(data)}
response = requests.post(url, headers=headers, data=data)
response.status_code

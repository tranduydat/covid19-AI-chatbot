import requests

url = 'https://api.fpt.ai/hmi/asr/general'
payload = open('', 'rb').read()
headers = {
    'api-key': 'FCGoI9nTM0FK0THmpETHxVIwrpobhv7X'
}

response = requests.post(url=url, data=payload, headers=headers)

print(response.json())

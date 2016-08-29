import requests
r = requests.post('http://127.0.0.1:8000/api-token-auth/',data={'username':'juan','password':'rootroot'})
print r.status_code
token=r.json()
print token['token']


r = requests.post('http://127.0.0.1:8000/api/v1/procesos/',headers={'Authorization':'JWT '+token['token']})
print r.status_code
print r.text



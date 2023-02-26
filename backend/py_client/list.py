from login import tokin_auth
import requests
import json


tokin_auth()

def call_list(ep):
    with open('creds.json') as json_file:
        data = json.load(json_file)
        access = data['access']
        cred = {
            "Authorization" : f"Bearer {access}"
        }
        print(access)
        ep = f"http://127.0.0.1:8000/accountallusers/{ep}"
        req_res = requests.get(ep, headers=cred)
        print(req_res.json())


call_list("normal/")







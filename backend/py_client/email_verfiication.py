import requests

endpoint = "http://127.0.0.1:8000/accountallusers/email-verification/"

cred = {"first_name":"ahmed", "last_name": "adel", "name": f"ahmed adel2{idx}",
         "email":f"desgro350@gmail.com", "password": "AhmedAd*86@3",
           "is_seller": "True", "is_normal":"False", "is_emp": "False", "is_male":"True","bdate":"2001-5-1"} #YYYY-MM-DD
auth_resp = requests.post(endpoint, json=cred)
print("done")
print(auth_resp.json())
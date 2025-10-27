import requests
import os
import json


url = "https://app.release.gensomerp.com/api/token"

payload = {
    "email": "bikash.sahoo@sharajman.com",
    "password": "Admin1234"
}
token_file = r"C:\Automation\gensom_scripts\backend\Login_Module\token.txt"

headers = {"Content-Type": "application/json"}

# response = {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzU5MjUyNjU0fQ.yPbifbk065Zh0297WiIDcyO-1_uioNid2IW43DxQMC4",
#   "menu_count": 48,
#   "name": "Bikash Sahoo",
#   "token_type": "bearer",
#   "user_type": "O&M TEAM"
# }



response = requests.post(url, json=payload, headers=headers)

print(response.status_code)

if response.status_code == 200:
  output = response.json()

  token = output.get("access_token")
  print(token)


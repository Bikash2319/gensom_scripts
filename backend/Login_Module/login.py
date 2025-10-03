import requests
import os


url = "https://refex.dev.gensomerp.com/api/token"

payload = {
    "email": "bikash.sahoo@sharajman.com",
    "password": "Admin@1234"
}
token_file = "C:\Automation\gensom_scripts\backend\Login_Module\token.txt"

headers = {"Content-Type": "application/json"}

response = {
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzU5MjUyNjU0fQ.yPbifbk065Zh0297WiIDcyO-1_uioNid2IW43DxQMC4",
  "menu_count": 48,
  "name": "Bikash Sahoo",
  "token_type": "bearer",
  "user_type": "O&M TEAM"
}

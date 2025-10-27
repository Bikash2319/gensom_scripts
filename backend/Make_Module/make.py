import requests

url = "https://refex.dev.gensomerp.com/api/create_make"
payload = {"make_name": "test make"}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzU5MjM0MzA0fQ.3pZ5CXwONUGV5fuuMxtPNd2FCcKu0E9UlH7HCs4uzTc"  # if required
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Status Code:", response.text)
 
# def add_new_make(make, token):
#     url = "https://refex.dev.gensomerp.com/api/create_make"
#     payload = {"make_name": f"{make}"}
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {token}"  # if required
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     print("Status Code:", response.status_code)
#     print("Status Code:", response.text)
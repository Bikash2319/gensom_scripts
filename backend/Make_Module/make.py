import requests
from backend.Utils.token import get_token



token = get_token()


url = "https://app.release.gensomerp.com/api/create_make"
payload = {"make_name": "test make"}
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Responses:", response.text)









# def add_new_make(make, token):
#     url = "https://refex.dev.gensomerp.com/api/create_make"
#     payload = {"make_name": f"{make}"}
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {token}"
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     print("Status Code:", response.status_code)
#     print("Status Code:", response.text)
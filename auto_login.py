from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from configurations import login

url = "https://refex.dev.gensomerp.com"


# #Inject token for authentication
# driver.get(f"{url}/login")
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzU4OTA2Mzg0fQ.KcNkP7mVhXtpq_QeL_SFf_QnILuOKAuEZE3voEtQ2TE"
# driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
# print("Login Successful")


login.log(url)

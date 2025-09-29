import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# TOKEN = "C:\\Automation\\gensom_scripts\\login\\token.txt"
TOKEN = r"C:\Automation\gensom_scripts\token.txt"

def read_token():
    if os.path.exists(TOKEN):
        with open(TOKEN, "r") as f:
            return f.read().strip()
    else:
        print("No token available.")     
    return None

def save_token(token):
    with open(TOKEN, "w") as f:
        f.write(token)

def login(driver, url):
    driver.get(f"{url}/login")

    #login with token
    token = read_token()
    print(token)
    if token:
        driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
        driver.get(f"{url}/dash")
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("dash"))
            print("Logged in with saved token")
            return
        except:
            print("Token expired or invalid, logging in with credentials...")

    #Login with credentials
    driver.get(f"{url}/login")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "floatingInputValue"))).send_keys("bikash.sahoo@sharajman.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
    driver.find_element(By.XPATH, "//button[text()='Login ']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("dash"))
    print("Logged in with credentials")

    #Save new token
    new_token = driver.execute_script("return window.localStorage.getItem('token');")
    if new_token:
        save_token(new_token)
        print(f"New token saved to token.txt : {new_token}")

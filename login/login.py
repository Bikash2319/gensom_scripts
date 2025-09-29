import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

TOKEN = "token.txt"

def read_token():
    """Read token from file if exists."""
    if os.path.exists(TOKEN):
        with open(TOKEN, "r") as f:
            return f.read().strip()
    return None

def save_token(token):
    """Save token to file (overwrite old one)."""
    with open(TOKEN, "w") as f:
        f.write(token)

def login(driver, url):
    driver.get(f"{url}/login")
    wait = WebDriverWait(driver, 20)

    # Step 1: Try login with token
    token = read_token()
    if token:
        driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
        driver.get(f"{url}/dash")  # go directly to dashboard
        try:
            wait.until(EC.url_contains("dash"))
            print("✅ Logged in with saved token")
            return
        except:
            print("⚠️ Token expired or invalid, logging in with credentials...")

    # Step 2: Login with credentials
    driver.get(f"{url}/login")
    wait.until(EC.visibility_of_element_located((By.ID, "floatingInputValue"))).send_keys("bikash.sahoo@sharajman.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
    driver.find_element(By.XPATH, "//button[text()='Login ']").click()

    wait.until(EC.url_contains("dash"))
    print("✅ Logged in with credentials")

    # Step 3: Save new token
    new_token = driver.execute_script("return window.localStorage.getItem('token');")
    if new_token:
        save_token(new_token)
        print("💾 New token saved to token.txt")

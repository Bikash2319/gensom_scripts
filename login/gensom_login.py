import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


TOKEN = "token.txt"
USERNAME = "bikash.sahoo@sharajman.com"
PASSWORD = "Admin@1234"


def read_token():
    """Read token from token.txt if exists."""
    if os.path.exists(TOKEN):
        with open(TOKEN, "r") as f:
            return f.read().strip()
    return None


def save_token(token):
    """Save token to token.txt (overwrite old one)."""
    with open(TOKEN, "w") as f:
        f.write(token)


def login_get_token(driver, url):
    """Login with credentials and return a fresh token."""
    driver.get(f"{url}/login")
    driver.find_element(By.ID, "floatingInputValue").send_keys(USERNAME)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Login ']").click()

    wait = WebDriverWait(driver, 20)
    wait.until(ec.url_contains("dash"))

    # get token from localStorage
    new_token = driver.execute_script("return window.localStorage.getItem('token');")

    # save to file
    save_token(new_token)
    print("✅ Logged in with credentials. Token updated in token.txt")

    return new_token


def login_with_token(driver, url):
    driver.get(f"{url}/login")
    token = read_token()

    if not token:
        print("⚠️ No token found. Logging in with credentials...")
        return login_get_token(driver, url)

    # inject token into localStorage
    driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
    driver.refresh()

    try:
        # wait to see if dashboard loads
        WebDriverWait(driver, 10).until(ec.url_contains("dash"))
        print("✅ Login successful with saved token")
        return token
    except Exception:
        # still on login page → token expired
        print("❌ Token expired. Logging in with credentials...")
        return login_get_token(driver, url)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "https://example.com"   # replace with your actual URL

    try:
        token = login_with_token(driver, url)
        print("🔑 Token in use:", token)
    finally:
        driver.quit()

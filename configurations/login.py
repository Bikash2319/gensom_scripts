
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
# driver = webdriver.Chrome()

    
def log(driver, url):
    print('dddddddddddddddddddddddddddddddddddddd')
    driver.get(f"{url}/login")
    driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
    driver.find_element(By.XPATH, "//button[text()='Login ']").click()
    wait = WebDriverWait(driver, 20)
    wait.until(ec.url_contains("dash"))
    token = driver.execute_script("return window.localStorage.getItem('token');")
    print(token,"999999999999999999999999")
    return token
    
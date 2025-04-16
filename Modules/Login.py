from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Gensom_login:

    RELEASE_URL = "https://release.gensom.sharajman.com/login"
    DEV_URL = "https://dev.gensom.sharajman.com/login"
    UAT_URL = "https://uat.gensom.sharajman.com/login"
    PROD_URL = "https://refex.gensomerp.com/login"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
    
    def login (self, url, email, password):
        self.driver.get(url)
        email_field = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        email_field.send_keys(email)
        password_field = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='password']")))
        password_field.send_keys(password)
        login_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text() = 'Login ']")))
        login_button.click()
        self.wait.until(ec.url_contains("dash"))

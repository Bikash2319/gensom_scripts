from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Setup:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
    
    def initialize_driver(self):
        self.driver.maximize_window()
        return self.driver, self.wait
    

    def log_into_release(self, dev):
        self.driver.get(dev)
        email = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        email.send_keys("bikash.sahoo@sharajman.com")
        password = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='password']")))
        password.send_keys("Admin@1234")
        login_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text() = 'Login ']")))
        login_button.click()
        self.wait.until(ec.url_contains("dash"))


    def log_into_production(self):
        self.driver.get("https://refex.gensomerp.com/login")
        email = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='email']")))
        email.send_keys("ashish.k@sharajman.com")
        password = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='password']")))
        password.send_keys("Admin1234")
        login_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[text() = 'Login ']")))
        login_button.click()
        self.wait.until(ec.url_to_be("https://refex.gensomerp.com/dash"))
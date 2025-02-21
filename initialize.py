from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from user_input import *
import time

driver = None  
wait = WebDriverWait (driver, 10)    

# def initialize_driver():
#     global driver
#     chrome_options = Options()
#     service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.maximize_window()
#     driver.implicitly_wait(10)

# def login():
#     global driver, wait # Access global variables
#     driver.get("https://release.gensom.sharajman.com/login")
#     driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
#     driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@12345")
#     driver.find_element(By.XPATH, "//button[text()='Login ']").click()
#     print("Login Successful")
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.url_contains("https://release.gensom.sharajman.com/dash")) 

class init:
    def init_login():
        chrome_options = Options()
        service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(release_url)
        driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@12345")
        driver.find_element(By.XPATH, "//button[text()='Login ']").click()
        print("Login Successful")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.url_contains("https://release.gensom.sharajman.com/dash")) 
        return driver, wait
    
    #Wait function
    def get_wait():
        return WebDriverWait(driver, 10)
            
    #Toaster 
    def toaster(driver):
        wait_toaster = WebDriverWait(driver, 10)
        toaster = wait_toaster.until(EC.visibility_of_element_located((By.ID, "toast-container")))
        print(f" {toaster.text}")
        toaster.click()
     
     #Save button   
    def save(driver):
        save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_button.click()
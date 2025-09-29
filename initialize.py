from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import openpyxl
import numpy as np
import math
 

class init:   
    def initialize(self):
        chrome_options = Options()
        service = Service(executable_path=r"C:\\Program Files\\Python\\Scripts\\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        return driver, wait
        
    def release_login(self,driver, wait):
        driver.get("https://release.gensom.sharajman.com/login")
        driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
        driver.find_element(By.XPATH, "//button[text()='Login ']").click()
        print("Login Successful")
        wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash"))
           
    #Toaster        
    def toaster(self, wait):
        try:
            toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
            print(f" {toaster.text}")
            toaster.click()
        except:
            print("No toaster message appeared.")  
             
     #Save button   
    def save(driver):
        save_button = driver.find_element(By.XPATH, "//button[text()=' Save ' or text()='Save']")
        save_button.click()
        print("SAve button clicked")
        
    def cancel(self, driver):
        cancel_button = driver.find_element(By.XPATH, "//button[text()=' Cancel ' or text()='Cancel']")
        cancel_button.click()
        print("Cancel button clicked")
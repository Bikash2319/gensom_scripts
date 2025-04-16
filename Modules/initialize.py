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



class Init:
    def save(self,driver):
        save_button = driver.find_element(By.XPATH, "//button[text()=' Save ' or text()='Save']")
        save_button.click()
        print("SAve button clicked")
        
    def cancel(self, driver):
        cancel_button = driver.find_element(By.XPATH, "//button[text()=' Cancel ' or text()='Cancel']")
        cancel_button.click()
        print("Cancel button clicked")
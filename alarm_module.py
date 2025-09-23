import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
import pandas as pd
import openpyxl

#setup
chrome_options = Options()
service = Service(executable_path=r"C:\\Program Files\\Python\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
#file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"

driver.get("https://refex.dev.gensomerp.com/login")
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzUyNTE2OTY1fQ.JxdztDKuW_URpTjsw7GM4_HoWqS_-jnuqEGbA9BCU3M"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")
driver.get("https://refex.dev.gensomerp.com/notification-list")

view_button = wait.until(EC.element_to_be_clickable/
            ((By.XPATH, "(//button[normalize-space(text())='View']/ancestor::*//span[normalize-space(text())='N/A'])[1]")))
view_button.click()

toggle_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//ngb-modal-window//label/span)[1]")))
toggle_button.click()

snooze_time = wait.until(EC.element_to_be_clickable((By.ID, "snoozeTime")))
snooze_time.send_keys("20")

technician_name = Select(wait.until(EC.element_to_be_clickable(By.XPATH, "//select[@formcontrolname='technician']")))
technician_name.select_by_visible_text(" Bikash Sahoo ")

approver_name = Select(wait.until(EC.element_to_be_clickable(By.XPATH, "//select[@formcontrolname='technician']")))
approver_name.select_by_visible_text(" Ashish Kumar ")

estimated_tat = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='tattime']")))
estimated_tat.send_keys("5")

notification_comment = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@formcontrolname='comments']")))
notification_comment.send_keys("Raised")

raise_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() =' Raise a Ticket ']")))
raise_button.click()


time.sleep(10)


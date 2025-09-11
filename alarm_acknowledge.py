import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select

#setup
chrome_options = Options()
service = Service(executable_path=r"C:\\Program Files\\Python\\Python313\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
#file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"

driver.get("https://refex.dev.gensomerp.com/login")
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzUyNzEwOTk0fQ.m39iapkvi0vI8w8iesXonyGyYm9ejQsgbNwjWWkPr0o"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")
driver.get("https://refex.dev.gensomerp.com/dash")

side_bar = wait.until(EC.element_to_be_clickable((By.XPATH, "//aside[@class='left-sidebar']")))
side_bar.click()

ticket_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//app-vertical-sidebar//li//a//span[text()='Ticket ']")))
ticket_menu.click()

notification_menu = wait.until(EC.element_to_be_clickable\
                                        ((By.XPATH, "//app-vertical-sidebar//a//span[text()='Notification Dashboard']")))
notification_menu.click()

view_button = wait.until(EC.element_to_be_clickable\
            ((By.XPATH, "(//button[normalize-space(text())='View']/ancestor::*//span[normalize-space(text())='N/A'])[1]")))
view_button.click()

snooze_time = wait.until(EC.element_to_be_clickable((By.ID, "snoozeTime")))
snooze_time.send_keys("20")

ackn_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Acknowledge ']")))
ackn_btn.click()


time.sleep(10)



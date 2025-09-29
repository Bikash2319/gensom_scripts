import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
service = Service(executable_path=r"C:\\Program Files\\Python\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = webdriver.ActionChains(driver)

driver.get("https://refex.dev.gensomerp.com/login")
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzUzMjgwNjE2fQ.R42RYhUfMw6ThlABw_Qq9JRb5WBRukBgqkEkv2cusnQ"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")
driver.get("https://refex.dev.gensomerp.com/dash")

side_bar = wait.until(EC.element_to_be_clickable((By.XPATH, "//aside[@aria-label='sidebar']")))
actions.move_to_element(side_bar).click().perform()

master_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-scrollbar//span[text()='Master ']")))
actions.move_to_element(master_menu).click().perform()

category_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-scrollbar//span[text()='Category']")))
actions.move_to_element(category_menu).click().perform()






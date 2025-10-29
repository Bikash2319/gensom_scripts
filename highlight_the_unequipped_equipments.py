import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 


chrome_options = Options()
service = Service(executable_path=r"C:\Program Files\Python\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://refex.dev.gensomerp.com/login")
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjoyNiwidXNlcl9pZCI6MzEsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzYxNzUyNDYwfQ.vIeQiv1zP3BD6eRChPwrATVbW4Hs2mfiheo6uTD-eQ8"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")
driver.get("https://refex.dev.gensomerp.com/plant-management/85/edit-plant")

equipment_tab = wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()='Equipment Details']")))
equipment_tab.click()

add_equipment = wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()=' Add Equipment ']")))
add_equipment.click()

search_equipment = wait.until(ec.element_to_be_clickable(driver.find_element(By.ID, "typeahead-format")))
search_equipment.send_keys("Major Equipment")
time.sleep(3)

suggestions = wait.until(ec.visibility_of_element_located((By.XPATH, "//ngb-typeahead-window | //div[contains(@id, 'ngb-typeahead-')]")))
time.sleep(3)
search_elements = suggestions.find_elements(By.TAG_NAME, "button")

# for item in search_elements:
#     print(item.text)

for item in search_elements:
    # driver.execute_script("arguments[0].style.border='3px solid red'; arguments[0].style.backgroundColor='green';", smb)
    # print("Found:", smb.text)
    # time.sleep(1)
    text = item.text.strip().lower()
    if "smb" in text:
        driver.execute_script(
            "arguments[0].style.border='3px solid green'; arguments[0].style.backgroundColor='lightgreen';", item)
    elif "inv" in text:
        driver.execute_script(
            "arguments[0].style.border='3px solid red'; arguments[0].style.backgroundColor='salmon';", item)
    else:
        driver.execute_script(
            "arguments[0].style.border='3px solid green'; arguments[0].style.backgroundColor='sky';", item)
    time.sleep(1.5)
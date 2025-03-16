from initialize import *
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Setup WebDriver
chrome_options = Options()
service = Service(executable_path=r"C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://release.gensom.sharajman.com/login")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash"))
driver.get("https://release.gensom.sharajman.com/make")

# # Inject token for authentication
# driver.get("https://refex.gensomerp.com/")
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2hpc2gua0BzaGFyYWptYW4uY29tIiwibG9naW5faWQiOjMsInVzZXJfaWQiOjMsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzQxODg1NzgwfQ.nw0vtsR4_IPiQSY5qz5q6MRE01tvFS2Cld0izs0nc2U"
# driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
# print("Login Successful")
# driver.get("https://refex.gensomerp.com/make")

# Read Excel file
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, "make", engine='openpyxl')

# Convert to list of dictionaries
data_list = df.to_dict(orient="records")
for item in data_list: 
    make = item.get("make").strip()
    # if not make:  # Skip empty makes
    #     print("Skipping empty make entry...")
    #     continue
    time.sleep(1)
    add_make_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']")))
    add_make_button.click()
    make_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Make Here']")))
    make_input.send_keys(make)
    init.save(driver)
    toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
    print(f"{toaster.text}")
    toaster.click()
    if toaster.text == "Make already exists." :
        init.cancel(driver)
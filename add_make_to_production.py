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
driver.get(release_url)
wait = WebDriverWait(driver, 10)

driver.get("https://release.gensom.sharajman.com/make")
# Inject token for authentication
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjo0LCJ1c2VyX2lkIjo0LCJ1c2VyX3R5cGUiOiJPJk0gVEVBTSIsImV4cCI6MTc0MTQ0MjM1Mn0.j9CISrtW-QjQRf-5FRA6EHnAkZWV0AsnwzuxOJcBSvI"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")

# Read Excel file
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Convert to list of dictionaries
data_list = df.to_dict(orient="records")

for item in data_list:
    
    # make = item.get("make", "").strip()
    # if not make:  # Skip empty makes
    #     print("Skipping empty make entry...")
    #     continue
    
    driver.find_element(By.XPATH, "//a[@href='/make']").click()
    print('Make master clicked')

    add_make_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']")))
    add_make_button.click()
    
    make_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Make Here']")))
    make_input.send_keys(make)
    
    try:
        init.save(driver)
        toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
        print(f"Toaster message: {toaster.text.strip()}")
        toaster.click()

        # If model already exists, cancel
        if toaster.text.strip().lower() == "this model combination already exists.":
            init.cancel(driver)
            toaster.click()

    except Exception as e:
        print("Error:", e)
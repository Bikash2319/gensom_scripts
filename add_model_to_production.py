# from initialize import *
# from user_input import *
# import pandas as pd

# chrome_options = Options()
# service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get(release_url)
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjo0LCJ1c2VyX2lkIjo0LCJ1c2VyX3R5cGUiOiJPJk0gVEVBTSIsImV4cCI6MTc0MTM3MjkwNX0.uUP90DHXEetKT8jsZUwBslUedzb1pZ8tPLlZXZJJU3s"
# driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
# # driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
# # driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
# # driver.find_element(By.XPATH, "//button[text()='Login ']").click()
# print("Login Successful")
# wait = WebDriverWait(driver, 10)

# # wait.until(EC.url_contains("https://release.gensom.sharajman.com/dash")) 
# #driver.get("https://release.gensom.sharajman.com/dash")
# driver.get("https://release.gensom.sharajman.com/model")
# file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
# df = pd.read_excel(file_path, engine='openpyxl')

# # Convert to list of dictionaries
# data_list = df.to_dict(orient="records")
# for item in data_list:
#     time.sleep(2)
#     wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[@ngbtooltip='Add Model']"))).click()

#     #make dropdown
    
#     select_make = Select(driver.find_element(By.ID, "make"))
#     select_make.select_by_visible_text(item.get("make"))

#     #category dropdown
   
#     select_category = Select (driver.find_element(By.ID, "category"))
#     select_category.select_by_visible_text(item.get("category"))

#     #sub category dropdown
    
#     select_sub_category = Select(driver.find_element(By.ID, "subCategory"))
#     select_sub_category.select_by_visible_text(item.get("sub_category"))

#     #enter model
#     driver.find_element(By.ID, "model").send_keys(item.get('model_name'))
    
#     try:
        
#         init.save(driver)
#         toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
#         print(f" {toaster.text}")
#         toaster.click()
        
#         if toaster.text == "this model combination already exists.":
#             init.cancel(driver)
#             toaster.click()
#     except Exception as e:
#         print(e)


from initialize import *
from user_input import *
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

# Inject token for authentication
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjo0LCJ1c2VyX2lkIjo0LCJ1c2VyX3R5cGUiOiJPJk0gVEVBTSIsImV4cCI6MTc0MTM3MjkwNX0.uUP90DHXEetKT8jsZUwBslUedzb1pZ8tPLlZXZJJU3s"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")

wait = WebDriverWait(driver, 10)
driver.get("https://release.gensom.sharajman.com/model")

# Read Excel file
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Convert to list of dictionaries
data_list = df.to_dict(orient="records")

for item in data_list:
    time.sleep(1)

    # Click 'Add Model' button
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Model']"))).click()

    # Select 'Make'
    make = item.get("make", "").strip()
    if make:
        select_make = Select(wait.until(EC.element_to_be_clickable((By.ID, "make"))))
        select_make.select_by_visible_text(make)

    # Select 'Category'
    category = item.get("category", "").strip()
    if category:
        select_category = Select(wait.until(EC.element_to_be_clickable((By.ID, "category"))))
        select_category.select_by_visible_text(category)

    # Select 'Sub-Category'
    sub_category = item.get("sub_category", "").strip()
    if sub_category:
        select_sub_category = Select(wait.until(EC.element_to_be_clickable((By.ID, "subCategory"))))
        select_sub_category.select_by_visible_text(sub_category)

    # Enter Model Name
    model_name = item.get("model_name", "").strip()
    driver.find_element(By.ID, "model").send_keys(model_name)

    # Save Model
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
       



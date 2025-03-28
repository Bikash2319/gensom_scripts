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
service = Service(executable_path=r"C:\Users\Bikash Chandra Sahoo\AppData\Local\Programs\Python\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://dev.gensom.sharajman.com/login")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait.until(EC.url_to_be("https://dev.gensom.sharajman.com/dash"))
driver.get("https://dev.gensom.sharajman.com/make")

# driver.get("https://refex.gensomerp.com/login")
# driver.find_element(By.ID, "floatingInputValue").send_keys("ashish.k@sharajman.com")
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin1234")
# driver.find_element(By.XPATH, "//button[text()='Login ']").click()
# print("Login Successful")
# wait.until(EC.url_to_be("https://refex.gensomerp.com/dash"))
# driver.get("https://refex.gensomerp.com/model")


# Read Excel file
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, "Model", engine='openpyxl')

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
    model_name = item.get("model_name", "")
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
       



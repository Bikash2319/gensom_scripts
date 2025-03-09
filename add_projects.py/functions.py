from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pandas as pd

environment = 'release'
url = f"https://{environment}.gensom.sharajman.com/login"

chrome_options = Options()
service = Service(executable_path=r"C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)    
actions = ActionChains(driver)

class gensom:
    def gensom_login():
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(url)
        driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
        driver.find_element(By.XPATH, "//button[text()='Login ']").click()
        print("Login Successful")
        wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash")) 
    
def toaster(wait):
        try:
            toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
            print(f" {toaster.text}")
            toaster.click()
        except:
            print("No toaster message appeared.")
            
def save(driver):
        save_button = driver.find_element(By.XPATH, "//button[text()=' Save ' or text()='Save']")
        save_button.click()
        print("SAve button clicked")
        
def cancel(driver):
    cancel_button = driver.find_element(By.XPATH, "//button[text()=' Cancel ' or text()='Cancel']")
    cancel_button.click()
    print("Cancel button clicked")

file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
variable = pd.read_excel(file_path, engine='openpyxl')
df = pd.read_excel(file_path, engine='openpyxl')

# Convert to list of dictionaries
data_list = df.to_dict(orient="records")
print(data_list,'*********************************')
# print(df.head())
make = variable.loc[0, 'Make Name']
category = variable.loc[1, 'Category Name']   


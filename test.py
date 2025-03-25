from initialize import *
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
import string

#setup
chrome_options = Options()
service = Service(executable_path=r"C:\Users\Bikash Chandra Sahoo\AppData\Local\Programs\Python\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

#login
driver.get("https://release.gensom.sharajman.com/login")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash"))


#Read Excel sheet
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, "Testing", engine='openpyxl')

driver.get("https://release.gensom.sharajman.com/plant-management/108/edit-plant")
equipment_tab = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()='Equipment Details']")))
equipment_tab.click()
print("Equipment tab clicked")

add_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()=' Add Equipment ']")))
add_equipment.click()
print("Add equipment button clicked")

search_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "typeahead-format")))
search_equipment.send_keys("Major Equipment")
time.sleep(2)

elements = search_equipment.find_elements(By.XPATH, "//ngb-typeahead-window//button")
dropdown_values = [option.text for option in elements]
dropdown_len=len(dropdown_values)
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
for i in range(0,dropdown_len):
    print(i)
    add_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()=' Add Equipment ']")))
    add_equipment.click()
    print("Add equipment button clicked")

    search_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "typeahead-format")))
    search_equipment.send_keys("Major Equipment")
    time.sleep(2)
    search_equipment.send_keys(Keys.ENTER)
    time.sleep(2)

    installation_date = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "installation_date")))
    installation_date.send_keys("01/01/2025")
    fetch = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//i[@class='fas fa-circle-notch']")))
    fetch.click()
    print('----------------------------------')
    
    data_logger_dd = Select(driver.find_element(By.ID, "data_logger_id"))
    data_logger_dd.select_by_visible_text("Logger 1")

    driver.find_element(By.XPATH, "//button[text()=' Add  ']").click()
 

    # elements = search_equipment.find_elements(By.XPATH, "//ngb-typeahead-window//button")
    # driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()






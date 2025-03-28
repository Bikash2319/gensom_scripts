from initialize import *
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
import string
import math

#setup
chrome_options = Options()
service = Service(executable_path=r"C:\Users\Bikash Chandra Sahoo\AppData\Local\Programs\Python\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

#login
driver.get("https://dev.gensom.sharajman.com/login")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait.until(EC.url_to_be("https://dev.gensom.sharajman.com/dash"))

# driver.get("https://refex.gensomerp.com/")
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2hpc2gua0BzaGFyYWptYW4uY29tIiwibG9naW5faWQiOjMsInVzZXJfaWQiOjMsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzQzMDk2ODg5fQ.5PEOHX_HgTV4CQ7yEV3v7E7Da5fx3DxGD4esOSX54rA"
# driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
# print("Login Successful")
# driver.get("https://refex.gensomerp.com/inventory-managment")

# driver.get("https://dev.gensom.sharajman.com/inventory-managment")
# #Read Excel sheet
# file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
# df = pd.read_excel(file_path, "Testing")

# # Convert to list of dictionaries
# data_list = df.to_dict(orient="records")

# for item in data_list:
      
#     time.sleep(1)
#     add_inventory_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Inventory']")))
#     add_inventory_button.click()
#     print("Add inventory button clicked")

#     time.sleep(0.5)
#     inventory_name = item.get("item_name")
#     inv_name = driver.find_element(By.ID, "inventory_name").send_keys(inventory_name)
#     make = item.get("make").strip()
#     select_make = Select(driver.find_element(By.ID, "make_id"))
#     select_make.select_by_visible_text(make)

#     model = item.get("model_name")
#     model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ng-select-container')]")))
#     model_dropdown.click()
#     model_option = driver.find_element(By.XPATH, f"//ng-dropdown-panel//div[contains(@class, 'ng-option') and span[text()='{model}']]")
#     model_option.click()
#     time.sleep(1)

#     subCategory_value = driver.find_element(By.ID, "sub_category_id")
#     sub_category_field = subCategory_value.get_attribute("textContent").strip()
#     #sub_category_field = driver.execute_script("return arguments[0].textContent;", subCategory_value)
#     print(f"Sub Category Retrieved: {sub_category_field}")
#     sub_category_text = sub_category_field.replace("Select Sub Category", "").strip()
#     print(f"sub category is :{sub_category_text}")
    
#     ac_capacity = str(item.get("ac_capacity", "0"))
#     dc_capacity = float(item.get("dc_capacity", "0"))
#     inv_type = item.get("inv_type", "")

#     if sub_category_text.lower() in ["inverters", "inverter"]:
#         time.sleep(1)
#         wait.until(EC.element_to_be_clickable((By.ID, "ac_capacity"))).send_keys(ac_capacity)
#         wait.until(EC.element_to_be_clickable((By.ID, "dc_capacity"))).send_keys(dc_capacity)
#         time.sleep(1)
#         inverter_type = Select(driver.find_element(By.ID, "inverter_type"))
#         inverter_type.select_by_visible_text(inv_type)
#         print("Inverter fields filled.")

#     elif sub_category_text.lower() == "string monitoring box":
        
#         wait.until(EC.element_to_be_clickable((By.ID, "ac_capacity"))).send_keys(ac_capacity)
#         factor = 10 ** 2
#         round_dc = math.ceil(dc_capacity * factor) / factor
#         wait.until(EC.element_to_be_clickable((By.ID, "dc_capacity"))).send_keys(round_dc)
#         print("SMB fields filled.")

#     elif sub_category_text.lower() in ["multi functional meter", "weather monitoring system"]:
#         print("No fields filled for MFM/WMS.")

#     else:
#         print("Unknown sub-category. No fields filled.")


#     w_name = item.get("warehouse").strip()
#     select_warehouse = Select(driver.find_element(By.ID, "warehouse_id"))
#     for option in select_warehouse.options:
#         if option.text.strip() == w_name:  
#             option.click()
#             break

#     serial_number = random.randint(10000, 99999)
#     driver.find_element(By.ID,"serial_no").send_keys(serial_number)
#     driver.find_element(By.ID, "reorder_no").send_keys("1")
#     driver.find_element(By.ID, "quantity").send_keys("1")

#     vendor = item.get("vendor").strip()
#     select_vendor = Select(driver.find_element(By.ID, "vendor_id"))
#     for option in select_vendor.options:
#         if option.text.strip() == vendor:  
#             option.click()
#             break 

#     po_number = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
#     driver.find_element(By.ID, "po_number").send_keys(po_number)
#     print(po_number)

#     init.save(driver)

#     toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
#     print(f"Toaster message: {toaster.text}")
#     toaster.click()
#     if toaster.text.strip() == 'This Inventory already exists':
#         init.cancel(driver)

driver.get("https://dev.gensom.sharajman.com/plant-management/5/edit-plant")
time.sleep(1)
equipment_tab = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()='Equipment Details']")))
equipment_tab.click()
print("Equipment tab clicked")

add_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()=' Add Equipment ']")))
add_equipment.click()
print("Add equipment button clicked")

search_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "typeahead-format")))
search_equipment.send_keys("Devices")
time.sleep(5)

elements = search_equipment.find_elements(By.XPATH, "//ngb-typeahead-window//button")
dropdown_values = [option.text for option in elements]
dropdown_len=len(dropdown_values)
close_modal = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[@aria-label='Close']")))
time.sleep(1)
close_modal.click()
for i in range(0,dropdown_len):
    print(i)
    add_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()=' Add Equipment ']")))
    add_equipment.click()
    print("Add equipment button clicked")

    search_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "typeahead-format")))
    search_equipment.send_keys("Devices")
    time.sleep(2)
    search_equipment.send_keys(Keys.ENTER)
    time.sleep(2)

    installation_date = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "installation_date")))
    installation_date.send_keys("01/01/2025")
    fetch = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//i[@class='fas fa-circle-notch']")))
    fetch.click()
    print('----------------------------------')
    
    data_logger_dd = Select(driver.find_element(By.ID, "data_logger_id"))
    data_logger_dd.select_by_visible_text("Logger-0011New")

    mounting_dd = Select(driver.find_element(By.ID, "mounting_type"))
    mounting_dd.select_by_visible_text("Fixed Tilt")

    driver.find_element(By.XPATH, "//button[text()=' Add  ']").click()
    time.sleep(0.5)





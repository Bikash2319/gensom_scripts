from initialize import *
import pandas as pd
import random
import string

#setup
chrome_options = Options()
service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# #login with credential
# driver.get("https://release.gensom.sharajman.com/login")
# driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
# driver.find_element(By.XPATH, "//button[text()='Login ']").click()
# print("Login Successful")
# wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash"))
# driver.get("https://release.gensom.sharajman.com/inventory-managment")

#Inject token for authentication
driver.get("https://refex.gensomerp.com/")
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2hpc2gua0BzaGFyYWptYW4uY29tIiwibG9naW5faWQiOjMsInVzZXJfaWQiOjMsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzQxNzk4OTY3fQ.SOYjzhfcbjDUZj3UvMFu7dnwISqj61Hi95N_uxlrfaU"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")
driver.get("https://refex.gensomerp.com/inventory-managment")

#Read Excel sheet
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, "Add Inventory", engine='openpyxl')

# Convert to list of dictionaries
data_list = df.to_dict(orient="records")

for item in data_list:
    print(item)

    time.sleep(1)
    add_inventory_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Inventory']")))
    add_inventory_button.click()
    print("Add inventory button clicked")

    time.sleep(0.5)
    inventory_name = item.get("item_name")
    inv_name = driver.find_element(By.ID, "inventory_name").send_keys(inventory_name)
    make = item.get("make").strip()
    select_make = Select(driver.find_element(By.ID, "make_id"))
    select_make.select_by_visible_text(make)

    model = item.get("model_name").strip()
    model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ng-select-container')]")))
    model_dropdown.click()
    model_option = driver.find_element(By.XPATH, f"//ng-dropdown-panel//div[contains(@class, 'ng-option') and span[text()='{model}']]")
    model_option.click()

    time.sleep(1)
    ac_capacity = str(item.get("ac_capacity", "0"))  
    dc_capacity = str(item.get("dc_capacity", "0"))
    subCategory_value = driver.find_element(By.ID, "sub_category_id")
    sub_category_field = subCategory_value.get_attribute("value").strip()
    print(f"Sub Category Retrieved: {sub_category_field}")
    
    # if sub_category_field in ('Inverters', 'INVERTER', 'inv', 'INV'):
    time.sleep(1)
    #driver.find_element(By.ID, "ac_capacity").send_keys(ac_capacity)
    wait.until(EC.element_to_be_clickable((By.ID, "ac_capacity"))).send_keys(ac_capacity)
    time.sleep(1)
    #driver.find_element(By.ID, "dc_capacity").send_keys(dc_capacity)
    wait.until(EC.element_to_be_clickable((By.ID, "dc_capacity"))).send_keys(dc_capacity)
    time.sleep(1)
    inverter_type = Select(driver.find_element(By.ID, "inverter_type"))
    inv_type = item.get("inv_type")
    print(inv_type)
    inverter_type.select_by_visible_text(inv_type)

    # elif sub_category_field in ('SMB', 'smb', 'String Monitoring Box', 'STRING MONITORING BOX', 'string monitoring box'):
    #     wait.until(EC.element_to_be_clickable((By.ID, "ac_capacity"))).send_keys(ac_capacity)
    #     wait.until(EC.element_to_be_clickable((By.ID, "dc_capacity"))).send_keys(dc_capacity)

    # elif sub_category_field in ('Multi Functional Meter', 'MULTI FUNCTIONAL METER', 'MFM', 'multi functional meter', 'wms', 'WMS', 'Weather Monitoring System', 'WEATHER MONITIORING SYSTEM', 'weather monitoring system'):
    #     print("It is mfm or wms.")

    w_name = item.get("warehouse")
    select_warehouse = Select(driver.find_element(By.ID, "warehouse_id"))
    for option in select_warehouse.options:
        if option.text.strip() == w_name:  
            option.click()
            break

    serial_number = random.randint(10000, 99999)
    driver.find_element(By.ID,"serial_no").send_keys(serial_number)
    driver.find_element(By.ID, "reorder_no").send_keys("1")
    driver.find_element(By.ID, "quantity").send_keys("1")

    vendor = item.get("vendor")
    select_vendor = Select(driver.find_element(By.ID, "vendor_id"))
    for option in select_vendor.options:
        if option.text.strip() == vendor:  
            option.click()
            break 

    po_number = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    driver.find_element(By.ID, "po_number").send_keys(po_number)
    print(po_number)

    init.save(driver)

    toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
    print(f"Toaster message: {toaster.text}")
    toaster.click()
    if toaster.text.strip() == 'This Inventory already exists':
        init.cancel(driver)
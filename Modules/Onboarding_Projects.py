from initialize import *
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#setup
chrome_options = Options()
service = Service(executable_path=r"C:\Users\Bikash Chandra Sahoo\AppData\Local\Programs\Python\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"


# #login
# driver.get("https://release.gensom.sharajman.com/login")
# driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
# driver.find_element(By.XPATH, "//button[text()='Login ']").click()
# print("Login Successful")
# wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash"))
# driver.get("https://release.gensom.sharajman.com/inventory-managment")


#Inject token for authentication
driver.get("https://refex.gensomerp.com/")
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2hpc2gua0BzaGFyYWptYW4uY29tIiwibG9naW5faWQiOjMsInVzZXJfaWQiOjMsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzQzNzg5OTg2fQ.CveaZKuSmwIA_tx2YYWzUW-_mQZAUQZCUGiAqkuWcWA"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")
driver.get("https://refex.gensomerp.com/inventory-managment")


df2 = pd.read_excel(file_path, "Add Inventory")
# Convert to list of dictionaries
data_list = df2.to_dict(orient="records")

for item in data_list:
      
    time.sleep(1)
    add_inventory_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Inventory']")))
    add_inventory_button.click()
    print("Add inventory button clicked")

    time.sleep(0.5)
    inventory_name = item.get("item_name")
    inv_name = driver.find_element(By.ID, "inventory_name").send_keys(inventory_name)
    make = item.get("make")
    select_make = Select(driver.find_element(By.ID, "make_id"))
    select_make.select_by_visible_text(make)

    model = item.get("model_name")
    model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ng-select-container')]")))
    model_dropdown.click()
    model_option = driver.find_element(By.XPATH, f"//ng-dropdown-panel//div[contains(@class, 'ng-option') and span[text()='{model}']]")
    model_option.click()
    time.sleep(1)

    subCategory_value = driver.find_element(By.ID, "sub_category_id")
    sub_category_field = subCategory_value.get_attribute("textContent").strip()
    #sub_category_field = driver.execute_script("return arguments[0].textContent;", subCategory_value)
    print(f"Sub Category Retrieved: {sub_category_field}")
    sub_category_text = sub_category_field.replace("Select Sub Category", "").strip()
    print(f"sub category is :{sub_category_text}")
    
    ac_capacity = str(item.get("ac_capacity", "0"))
    dc_capacity = str(item.get("dc_capacity", "0"))
    inv_type = item.get("inv_type", "")

    if sub_category_text.lower() in ["inverters", "inverter"]:
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, "ac_capacity"))).send_keys(ac_capacity)
        wait.until(EC.element_to_be_clickable((By.ID, "dc_capacity"))).send_keys(dc_capacity)
        time.sleep(1)
        inverter_type = Select(driver.find_element(By.ID, "inverter_type"))
        inverter_type.select_by_visible_text(inv_type)
        print("Inverter fields filled.")

    elif sub_category_text.lower() == "string monitoring box":
        wait.until(EC.element_to_be_clickable((By.ID, "ac_capacity"))).send_keys(ac_capacity)
        wait.until(EC.element_to_be_clickable((By.ID, "dc_capacity"))).send_keys(dc_capacity)
        print("SMB fields filled.")

    elif sub_category_text.lower() in ["multi functional meter", "weather monitoring system"]:
        print("No fields filled for MFM/WMS.")

    else:
        print("Unknown sub-category. No fields filled.")


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

    Init.save(driver)
    time.sleep(0.5)

    toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
    print(f"Toaster message: {toaster.text}")
    toaster.click()
    if toaster.text.strip() == 'This Inventory already exists':
        Init.cancel(driver)
    


#Read Excel sheet
df1 = pd.read_excel(file_path, "Add Project")

# Convert to list of dictionaries
data_list = df1.to_dict(orient="records")

for item in data_list:
    try:
        #driver.get("https://release.gensom.sharajman.com/plant-management")
        driver.get("https://refex.gensomerp.com/plant-management")
        time.sleep(1)
        add_project_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Project']")))
        add_project_button.click()
        print("Add project button clicked")

        #Basic details tab
        driver.find_element(By.XPATH, "//button[text()='Basic Details']")
        
        plant_name = item.get("project_name").strip()
        driver.find_element(By.ID, "plant_name").send_keys(plant_name)
        
        s_name = item.get("project_short_name").strip()
        driver.find_element(By.ID, "short_name").send_keys(s_name)
        
        p_add = item.get("site_address")
        driver.find_element(By.ID, "site_address").send_keys(p_add)
        
        p_lat = item.get("latitude")
        driver.find_element(By.ID, "latitude").send_keys(p_lat)
        
        p_long = item.get("longitude")
        driver.find_element(By.ID, "longitude").send_keys(p_long)

        p_type = driver.find_element(By.ID, "domain")
        select_type = Select(p_type)
        select_type.select_by_visible_text("Solar Management System")

        time.sleep(1)
        select_subtype = Select(driver.find_element(By.ID, "subdomain"))
        select_subtype.select_by_value("SOLAR_POWER_STORAGE")

        time.sleep(1)
        select_techno = Select(driver.find_element(By.ID, "technology_type"))
        select_techno.select_by_value("MONOCRYSTALLINE")

        time.sleep(1)
        i_type = item.get("installation_type")
        select_install = Select(driver.find_element(By.ID, "installation_type"))
        select_install.select_by_value(i_type)

        time.sleep(1)
        select_mount = Select(driver.find_element(By.ID, "mounting_type"))
        select_mount.select_by_value("FIXED TILT")

        tilt = item.get("tilt")
        driver.find_element(By.ID, "tilt_azimuth").send_keys(tilt)
        
        dc_cap = item.get("dc_capacity")
        driver.find_element(By.ID, "dc_capacity").send_keys(dc_cap)
        
        ac_cap = item.get("ac_capacity")
        driver.find_element(By.ID, "ac_capacity").send_keys(ac_cap)

        #comm_date = item.get("commissioning_date")
        driver.find_element(By.ID, "commissioning_date").send_keys("03/03/2025")
        
        w_name = item.get("warehouse")
        driver.find_element(By.ID, "warehouse").send_keys(w_name)

        # driver.find_element(By.ID, "is_wms_installed").click()
        # driver.find_element(By.ID, "is_smb_installed").click()
        
        start_time = item.get("start_time")
        driver.find_element(By.ID, "start_time").send_keys(start_time)
        
        end_time = item.get("end_time")
        driver.find_element(By.ID, "end_time").send_keys(end_time)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
        time.sleep(2)
        
        #-------------------------------------Add Data Logger Details----------------------------------

        Logger = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()='Data Logger Details']")))
        Logger.click()

        add_logger = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//button[text()=' Add Logger ']")))
        add_logger.click()

        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Logger No']").send_keys("Logger 1")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Block Name']").send_keys("Block 1")

        time.sleep(1)
        logger_make = item.get("logger_make")
        make_dd = Select(wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "make_id"))))
        make_dd.select_by_visible_text(logger_make)
        time.sleep(1.5)

        logger_model = item.get("logger_model")
        model_dd = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "[bindvalue='model_id']")))

        actions = ActionChains(driver)
        actions.click(model_dd).send_keys(logger_model).send_keys(Keys.ENTER).perform()

        connectivity = Select(driver.find_element(By.ID, "internet_connectivity"))
        connectivity.select_by_visible_text("Wi-fi")

        dev_num = random.randint(10000, 99999)
        driver.find_element(By.ID, "device_serial_no").send_keys(dev_num)

        driver.find_element(By.ID, "folder_path_to_ftp").send_keys("D:\ftp\logger")

        wms = Select(driver.find_element(By.ID,"wms_available"))
        wms.select_by_visible_text("Yes")

        plant = Select(driver.find_element(By.ID, "plant_curlainment"))
        plant.select_by_visible_text("Yes")

        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        #driver.back()
        #driver.find_element(By.XPATH("//button[text()= ' Cancel ']")).click()
        print(f"{plant_name} and data logger added")
        time.sleep(1)

        #-----------------------Add Equipment Details-------------------------------
        
        equipment_tab = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()='Equipment Details']")))
        equipment_tab.click()
        print("Equipment tab clicked")

        add_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()=' Add Equipment ']")))
        add_equipment.click()
        print("Add equipment button clicked")

        search_equipment = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "typeahead-format")))
        search_equipment.send_keys("Major Equipment")
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
            search_equipment.send_keys("Major Equipment")
            time.sleep(2)
            search_equipment.send_keys(Keys.ENTER)
            time.sleep(2)

            installation_date = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "installation_date")))
            installation_date.send_keys("01/01/2025")
            fetch = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//i[@class='fas fa-circle-notch']")))
            fetch.click()
            
            
            data_logger_dd = Select(driver.find_element(By.ID, "data_logger_id"))
            data_logger_dd.select_by_visible_text("Logger 1")

            driver.find_element(By.XPATH, "//button[text()=' Add  ']").click()
    
    except Exception as e:
        print(f"Error adding project {item.get('project_name')}: {e}")


driver.close()
        


        
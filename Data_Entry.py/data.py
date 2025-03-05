from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
import time

dev_url = "https://uat.gensom.sharajman.com/login"

chrome_options = Options()
service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(dev_url)
driver.find_element(By.ID, "floatingInputValue").send_keys("ashish.k@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait = WebDriverWait(driver, 20)
wait.until(EC.url_to_be("https://uat.gensom.sharajman.com/dash"))

w_name = 'Kishangarh Site Warehouse'
plant_name = 'DH Kishangarh'
s_name = 'REIL017'
p_add = "Bikaner, Rajasthan"
p_lat = '53.526'
p_long = '85.69'
tilt = '5.33'
ac_cap = '50'
dc_cap = '51'
comm_date = '02-05-2025'
start_time = '05:00'
end_time = '19:00'

driver.get("https://uat.gensom.sharajman.com/plant-management")
add_project_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Project']")))
add_project_button.click()
print("Add project button clicked")
driver.find_element(By.XPATH, "//button[text()='Basic Details']")
driver.find_element(By.ID, "plant_name").send_keys(plant_name)
driver.find_element(By.ID, "short_name").send_keys(s_name)
driver.find_element(By.ID, "site_address").send_keys(p_add)
driver.find_element(By.ID, "latitude").send_keys(p_lat)
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
select_install = Select(driver.find_element(By.ID, "installation_type"))
select_install.select_by_value("ROOFTOP")
time.sleep(1)
select_mount = Select(driver.find_element(By.ID, "mounting_type"))
select_mount.select_by_value("FIXED TILT")
driver.find_element(By.ID, "tilt_azimuth").send_keys(tilt)
driver.find_element(By.ID, "dc_capacity").send_keys(dc_cap)
driver.find_element(By.ID, "ac_capacity").send_keys(ac_cap)
driver.find_element(By.ID, "commissioning_date").send_keys(comm_date)
driver.find_element(By.ID, "warehouse").send_keys(w_name)
driver.find_element(By.ID, "is_wms_installed").click()
driver.find_element(By.ID, "is_smb_installed").click()
driver.find_element(By.ID, "start_time").send_keys(start_time)
driver.find_element(By.ID, "end_time").send_keys(end_time)
driver.find_element(By.XPATH, "//button[text()=' Save ']").click()          
           
# warehouse_type = 'INTERNAL'
# warehouse_sub_type = 'NATIONAL'
# w_name = 'Kishangarh Site Warehouse'
# w_city = "Kishangarh"
# # latitude = ""
# # longitude = ""
# warehouse_address = "Kishangarh, Rajasthan"
# driver.get("https://uat.gensom.sharajman.com/warehouse")

# add_warehouse_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Warehouse']")))
# add_warehouse_button.click()
# print("Add warehouse button clicked")

# type_dropdown = Select(driver.find_element(By.ID, "warehouse_type"))
# sub_type_dropdown = Select(driver.find_element(By.ID, "warehouse_sub_type"))

# if warehouse_type == "INTERNAL":
#     type_dropdown.select_by_visible_text("INTERNAL")
#     print("Internal warehouse selected.")
# elif warehouse_type == "EXTERNAL":
#     type_dropdown.select_by_visible_text("EXTERNAL")
#     print("External warehouse selected.")
#     sub_type_dropdown.select_by_visible_text(warehouse_sub_type)
#     print(f'{warehouse_sub_type} is selected')
          

# driver.find_element(By.ID,"warehouse_name").send_keys(w_name)
# country = Select(driver.find_element(By.ID, "country"))
# country.select_by_value("1")

# driver.find_element(By.ID, "city").send_keys(w_city)
# # driver.find_element(By.ID, "latitude").send_keys(latitude)
# # driver.find_element(By.ID, "longitude").send_keys(longitude)
# driver.find_element(By.ID, "warehouse_address").send_keys(warehouse_address)

# driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
# print('warehouse added')
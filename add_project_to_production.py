import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd

#setup
chrome_options = Options()
service = Service(executable_path=r"C:\\Program Files\\Python313\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

#login
driver.get("https://refex.dev.gensomerp.com")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait.until(EC.url_contains("dash"))
driver.get("https://refex.dev.gensomerp.com/plant-management")


# #Inject token for authentication
# driver.get("https://refex.gensomerp.com/")
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2hpc2gua0BzaGFyYWptYW4uY29tIiwibG9naW5faWQiOjMsInVzZXJfaWQiOjMsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzQyNTkwODAzfQ.zZTExlpaIMOUxXjuwhyfjypBL6a43me_1R_rk_yWPAM"
# driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
# print("Login Successful")
# driver.get("https://refex.gensomerp.com/plant-management")

#Read Excel sheet
file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, "Add Project", engine='openpyxl')

# Convert to list of dictionaries
data_list = df.to_dict(orient="records")


for item in data_list:
    time.sleep(1)
    add_project_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Project']")))
    add_project_button.click()
    print("Add project button clicked")

    #Basic details tab
    driver.find_element(By.XPATH, "//button[text()='Basic Details']")
    
    plant_name = item.get("project_name")
    driver.find_element(By.ID, "plant_name").send_keys(plant_name)
    
    s_name = item.get("project_short_name")
    driver.find_element(By.ID, "short_name").send_keys(s_name)
    
    p_add = item.get("site_address")
    driver.find_element(By.ID, "site_address").send_keys(p_add)
    
    p_lat = item.get("latitude")
    driver.find_element(By.ID, "latitude").send_keys(p_lat)
    
    p_long = item.get("longitude")
    driver.find_element(By.ID, "longitude").send_keys(p_long)

    cluster = Select(driver.find_element(By.ID, "cluster"))
    cluster.select_by_visible_text("REIL")

    company = Select(driver.find_element(By.ID, "company"))
    company.select_by_visible_text("Refex")

    p_type = driver.find_element(By.ID, "domain")
    select_type = Select(p_type)
    select_type.select_by_visible_text("Solar Management System")

    time.sleep(2)
    select_subtype = Select(driver.find_element(By.ID, "subdomain"))
    select_subtype.select_by_value("SOLAR_POWER_STORAGE")

    time.sleep(2)
    select_techno = Select(driver.find_element(By.ID, "technology_type"))
    select_techno.select_by_value("MONOCRYSTALLINE")

    time.sleep(2)
    i_type = item.get("installation_type")
    select_install = Select(driver.find_element(By.ID, "installation_type"))
    select_install.select_by_value(i_type)

    time.sleep(2)
    select_mount = Select(driver.find_element(By.ID, "mounting_type"))
    select_mount.select_by_value("FIXED TILT")

    tilt = item.get("tilt")
    driver.find_element(By.ID, "tilt_azimuth").send_keys(tilt)
    
    dc_cap = item.get("dc_capacity")
    driver.find_element(By.ID, "dc_capacity").send_keys(dc_cap)
    
    ac_cap = item.get("ac_capacity")
    driver.find_element(By.ID, "ac_capacity").send_keys(ac_cap)

    #comm_date = item.get("commissioning_date")
    driver.find_element(By.ID, "commissioning_date").send_keys("2025-03-11")
    
    w_name = item.get("warehouse")
    driver.find_element(By.ID, "warehouse").send_keys(w_name)

    tarrif = item.get("tarrif")
    driver.find_element(By.ID, "tariff").send_keys(tarrif)

    data_frequency = Select(driver.find_element(By.ID, "data_frequency"))
    data_frequency.select_by_visible_text("5 Minutes")

    # driver.find_element(By.ID, "is_wms_installed").click()
    # driver.find_element(By.ID, "is_smb_installed").click()
    
    start_time = item.get("start_time")
    driver.find_element(By.ID, "start_time").send_keys(start_time)
    
    end_time = item.get("end_time")
    driver.find_element(By.ID, "end_time").send_keys(end_time)
    
    time.sleep(200)
    
    # init.save(driver)
    # time.sleep(2)
    # driver.back()
    # # driver.find_element(By.XPATH("//button[text()= ' Cancel ']")).click()
    # print(f"{plant_name} is added")
    
    
    

    
        
from initialize import *
from user_input import *

driver, wait = init.init_login()

driver.get("https://release.gensom.sharajman.com/plant-management")

add_project_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Project']")))
add_project_button.click()
print("Add project button clicked")

#Basic details tab
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
select_install.select_by_value("GROUND MOUNT")

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

# toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
# print(f" {toaster.text}")
# toaster.click()
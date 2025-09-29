from initialize import *
from user_input import *

driver , wait = init.init_login()

driver.get("https://release.gensom.sharajman.com/inventory-managment")

add_inventory_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Inventory']")))
add_inventory_button.click()
print("Add inventory button clicked")

driver.find_element(By.ID, "inventory_name").send_keys(inventory_name)

select_make = Select(driver.find_element(By.ID, "make_id"))
select_make.select_by_visible_text(make)

model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ng-select-container')]")))
time.sleep(3)
model_dropdown.click()

model_option = driver.find_element(By.XPATH, f"//ng-dropdown-panel//div[contains(@class, 'ng-option') and span[text()='{model}']]")
model_option.click()

subCategory_field = driver.find_element(By.ID, "sub_category_id")
if subCategory_field.text == 'Inverter' or 'INVERTER' or 'inv' or 'INV':
    inverter_type = Select(driver.find_element(By.ID, "inverter_type"))
    inverter_type.select_by_visible_text(inv_type)
    driver.find_element(By.ID, "ac_capacity").send_keys(ac_capacity)
    driver.find_element(By.ID, "dc_capacity").send_keys(dc_capacity)
    
elif subCategory_field.text == 'SMB' or 'smb' or 'String Monitoring Box' or 'STRING MONITORING BOX' or 'string monitoring box':
    driver.find_element(By.ID, "ac_capacity").send_keys(ac_capacity)
    driver.find_element(By.ID, "dc_capacity").send_keys(dc_capacity)

select_warehouse = Select(driver.find_element(By.ID, "warehouse_id"))
select_warehouse.select_by_visible_text(w_name)

driver.find_element(By.ID,"serial_no").send_keys(serial_no)
driver.find_element(By.ID, "reorder_no").send_keys(reorder_point)
driver.find_element(By.ID, "quantity").send_keys(quantity)

select_vendor = Select(driver.find_element(By.ID, "vendor_id"))
select_vendor.select_by_value("59")

driver.find_element(By.ID, "po_number").send_keys(po_number)

init.save(driver)
init.toaster(wait)


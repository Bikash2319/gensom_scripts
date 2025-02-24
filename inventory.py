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

model_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@placeholder='Select model']")))
model_dropdown.click()
print("----------------------------------------")
# Wait for the dropdown panel to appear
dropdown_model = wait.until(EC.presence_of_element_located((By.XPATH, "//ng-dropdown-panel[contains(@class, 'ng-dropdown-panel')]")))

# Select option by text
text = "Inv Solis 50k"
select_model_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'ng-option') and span[text()='{text}']]")))
#select_model_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ng-option') and span[text()='Inv Solis 50k']]")))
select_model_option.click()
print("*****************************************************************")

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


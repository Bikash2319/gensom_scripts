from initialize import *
from user_input import *



driver , wait = init.init_login()

driver.get("https://release.gensom.sharajman.com/warehouse")

add_warehouse_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Warehouse']")))
add_warehouse_button.click()
print("Add warehouse button clicked")

type_dropdown = Select(driver.find_element(By.ID, "warehouse_type"))
sub_type_dropdown = Select(driver.find_element(By.ID, "warehouse_sub_type"))

if warehouse_type == "INTERNAL":
    type_dropdown.select_by_visible_text("INTERNAL")
    print("Internal warehouse selected.")
elif warehouse_type == "EXTERNAL":
    type_dropdown.select_by_visible_text("EXTERNAL")
    print("External warehouse selected.")
    sub_type_dropdown.select_by_visible_text(warehouse_sub_type)
    print(f'{warehouse_sub_type} is selected')
          

driver.find_element(By.ID,"warehouse_name").send_keys(w_name)
country = Select(driver.find_element(By.ID, "country"))
country.select_by_value("1")

driver.find_element(By.ID, "city").send_keys(w_city)
driver.find_element(By.ID, "latitude").send_keys(latitude)
driver.find_element(By.ID, "longitude").send_keys(longitude)
driver.find_element(By.ID, "warehouse_address").send_keys(warehouse_address)

driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
print('warehouse added')

toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f" {toaster.text}")
toaster.click()
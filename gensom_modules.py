from initialize import *
from user_input import *
from selenium.webdriver.common.action_chains import ActionChains


driver , wait = init.init_login()

actions = ActionChains(driver)

side_bar = driver.find_element(By.XPATH, "//aside[1]//ng-scrollbar//div")
master_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Master ')]")
management_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Management ')]")

actions.move_to_element(side_bar).click().perform()
actions.move_to_element(master_menu).click().perform()

#Click on make option from sidebar
driver.find_element(By.XPATH, "//a[@href='/make']").click()
print('Make master clicked')

add_make_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']")))
add_make_button.click()
print('Add make button clicked')

make_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Make Here']")))
make_input.send_keys(make)
print('Make entered')

init.save(driver)
toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f"{toaster.text}")
toaster.click()

if toaster.text == "Make already exists." :
    init.cancel(driver)
    
wait.until(EC.element_to_be_clickable(side_bar))
side_bar.click()
print('Sidebar is clicked')

#Click on category option from sidebar
driver.find_element(By.XPATH, "//a[@href='/category-master']").click()
print('Category master is clicked')

add_category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Category']")))
add_category_button.click()

add_category = wait.until(EC.visibility_of_element_located((By.ID, "catType")))
add_category.send_keys(category)

init.save(driver)
toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f"{toaster.text}")
toaster.click()
if toaster.text == "Category already exists.":
    init.cancel(driver)

side_bar.click()
print('Sidebar is clicked')

#Click on sub category master
driver.find_element(By.XPATH, "//a[@href='/subcategory-master']").click()
print('Subcategory master is clicked')
driver.find_element(By.XPATH, "//div[@ngbtooltip='Add SubCategory']").click()
print('Add subcategory button is clicked')

cat_dropdown = driver.find_element(By.ID, "catType")
select_category = Select(cat_dropdown)
select_category.select_by_visible_text(category)

driver.find_element(By.ID, "subCat").send_keys(sub_category)

driver.find_element(By.ID, "recordlevel").click()
driver.find_element(By.ID, "serialnumber").click()
driver.find_element(By.ID, "tilt").click()
driver.find_element(By.ID, "mounting").click()

init.save(driver)
toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f"{toaster.text}")
subcat_toaster = toaster.text
print(subcat_toaster)
toaster.click()
if subcat_toaster == "Sub Category already exists under this parent":
    cancel_button = driver.find_element(By.XPATH, "//button[text()=' Cancel ' or text()='Cancel']")
    cancel_button.click()
    print("Cancel button clicked")

wait.until(EC.element_to_be_clickable(side_bar))
side_bar.click()
print('Sidebar is clicked')

#Click model master form sidebar
driver.find_element(By.XPATH, "//a[@href='/model']").click()
print('Model master is clicked')

driver.find_element(By.XPATH, "//div[@ngbtooltip='Add Model']").click()
print('Add model button is clicked')

#make dropdown
make_dropdown = driver.find_element(By.ID, "make")
select_make = Select(make_dropdown)
select_make.select_by_visible_text(make)
print('Make is selected')

#category dropdown
category_dropdown = driver.find_element(By.ID, "category")
select_category = Select (category_dropdown)
select_category.select_by_visible_text(category)
print('Category is selected')

#sub category dropdown
sub_category_dropdown = driver.find_element(By.ID, "subCategory")
select_sub_category = Select(sub_category_dropdown)
select_sub_category.select_by_visible_text(sub_category)
print('Sub category is selected')

#enter model
driver.find_element(By.ID, "model").send_keys(model)
print('Model is entered')

init.save(driver)

toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f"{toaster.text}")
toaster.click()

if toaster.text == "this model combination already exists.":
    init.cancel(driver)
    print('Cancel button is clicked')
    
side_bar.click()

#click on management 
management_menu.click()

driver.find_element(By.XPATH, "//a[@href='/vendor-managment']").click()
print('Vendor Management is clicked')

driver.find_element(By.XPATH, "//button[text()='Add Vendor Type ']").click()                #add vendor type 

driver.find_element(By.XPATH, "//div[@ngbtooltip='Add Vendor type']").click()               #add vendor type button

driver.find_element(By.ID, "VendorType").send_keys(vendor_type)                             #Enter vendor type
driver.find_element(By.ID, "issubreq").click()                                              #Sub category required checkbox

init.save(driver)
toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f"{toaster.text}")
toaster.click()

if toaster.text == "Vendor type is already exists.":
    init.cancel(driver)

driver.back()                                                                             #navigate to back page
time.sleep(2)
add_vendor_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Vendor']")))
add_vendor_button.click()
print("Add vendor button clicked")

driver.find_element(By.ID, "name").send_keys(vendor_name)
driver.find_element(By.ID, "contactPerson").send_keys(contact_person)
select_vType = Select(driver.find_element(By.ID, "vType"))
select_vType.select_by_visible_text(vendor_type)

driver.find_element(By.ID, "ldNo").send_keys(landline_number)
driver.find_element(By.ID,"contactNumber").send_keys(contact_number)
driver.find_element(By.ID, "email").send_keys(vendor_email_id)

select_category = Select(driver.find_element(By.ID, "Classification"))
select_category.select_by_visible_text(category)

select_subcat = Select(driver.find_element(By.ID, "subclassification"))
select_subcat.select_by_visible_text(sub_category)

driver.find_element(By.ID, "communicationAddress").send_keys(comm_add)
select_comm_country = Select(driver.find_element(By.ID, "country"))
select_comm_country.select_by_value("1")

select_comm_state = Select(driver.find_element(By.ID, "state"))
select_comm_state.select_by_visible_text(comm_state)

if(same_as_billing_add == 1):
    driver.find_element(By.ID, "sameAsBilling").click()
else:
    driver.find_element(By.ID, "billingAddress").send_keys(bill_add)
    select_bill_country = Select(driver.find_element(By.ID, "billingCountry"))
    select_bill_country.select_by_value("1")
    select_bill_state = Select(driver.find_element(By.ID, "billingstate"))
    select_bill_state.select_by_visible_text(bill_state)


dropdown_xpath = "//div[contains(@class, 'ng-select-container')]"
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
dropdown.click()

# Wait and select "Battery Setup"
battery_setup_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Battery Setup']]"
battery_setup = wait.until(EC.element_to_be_clickable((By.XPATH, battery_setup_xpath)))
battery_setup.click()

dropdown.click()
# Wait and select "Oil Filtration"
oil_filtration_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Oil Filtration']]"
oil_filtration = wait.until(EC.element_to_be_clickable((By.XPATH, oil_filtration_xpath)))
oil_filtration.click()

dropdown.click()
# Wait and select "Cable Configuration"
Cable_Configuration_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Cable Configuration']]"
Cable_Configuration = wait.until(EC.element_to_be_clickable((By.XPATH, Cable_Configuration_xpath)))
Cable_Configuration.click()

init.save(driver)
toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f"{toaster.text}")
toaster.click()

side_bar.click()
master_menu.click()

driver.find_element(By.XPATH, "//a[@href='/warehouse']").click()            #Click on warehouse master menu
driver.find_element(By.XPATH, "//div[@ngbtooltip='Add Warehouse']").click() #Click on add warehouse button

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

if toaster.text == " This Warehouse already exists ":
    init.cancel(driver)

side_bar.click()
#master_menu.click()
driver.find_element(By.XPATH, "//a[@href='/inventory-managment']").click()      #Click on inventory management

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
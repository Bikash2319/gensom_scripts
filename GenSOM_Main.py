from initialize import *
from user_input import *
import vendor_management as vm
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
vm.vendor.add_new_vendor()
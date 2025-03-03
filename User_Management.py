from initialize import *
from user_input import *
from webelements import *

driver, wait = init.init_login()

driver.get("https://release.gensom.sharajman.com/manage-users")

driver.find_element(By.XPATH, "//div[@ngbtooltip='Add User']").click()

driver.find_element(By.XPATH, "//input[@formcontrolname='first_name']").send_keys(first_name)
driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']").send_keys(last_name)
driver.find_element(By.ID, "email").send_keys(vendor_email_id)
driver.find_element(By.ID, "contact_number").send_keys(contact_number)

select_department = Select(driver.find_element(By.ID, "department"))
select_department.select_by_value("1")

select_designation = Select(driver.find_element(By.ID, "designation"))
select_designation.select_by_value("1")

select_uType = Select(driver.find_element(By.ID, "userType"))
select_uType.select_by_value("GUEST USER")

driver.find_element(By.ID, "identity_number").send_keys(identity_number)

project_dropdown = driver.find_element(By.XPATH,"//div[contains(@class, 'ng-select-container')]")
project_dropdown.click()

select_option1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='AIR JAIPUR']]")))
select_option1.click()

project_dropdown.click()
select_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='AIR MANALI']]")))
select_option2.click()

enrollment_dd = Select(driver.find_element(By.ID, "enrollment"))
enrollment_dd.select_by_value(enrollment_type)


if enrollment_type == 'INTERNAL':
    select_role_type = Select(driver.find_element(By.ID,"role_type"))
    select_role_type.select_by_value('ADMIN')
elif enrollment_type == 'EXTERNAL':
    select_role_type = Select(driver.find_element(By.ID,"role_type"))
    select_role_type.select_by_value('CLIENT')
    
    driver.find_element(By.ID, "rate").send_keys('1000')
    driver.find_element(By.ID, "skill").send_keys(skills)
    
    
    driver.find_element(By.ID, "contract_number").send_keys(contract_number)
    
    select_currency = Select(driver.find_element(By.ID, "currency"))
    select_currency.select_by_value('Rs')

    select_country = Select(driver.find_element(By.ID, "country"))
    select_country.select_by_value("1")

    driver.find_element(By.ID, "companyName").send_keys(company_name)
    driver.find_element(By.ID, "loginAccess").click()
    

init.save(driver)

init.toaster(wait)




time.sleep(3)
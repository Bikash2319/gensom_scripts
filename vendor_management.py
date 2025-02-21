from initialize import *
from user_input import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(release_url)
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@12345")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("https://release.gensom.sharajman.com/dash")) 
print("Redirected to overview dashboard page")

driver.get("https://release.gensom.sharajman.com/vendor-managment")

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


select_activityTag = Select(driver.find_element(By.XPATH, "//ng-select[@placeholder='Select Activity']"))
battery_setup = driver.find_element(By.XPATH, "//span[contains(text(), 'Battery Setup')]")
battery_setup.click()


# driver.find_element(By.XPATH, "//ng-select[@placeholder='Select Activity']").click()
# battery_setup = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="a88e1315178d-0"]/span')))
# battery_setup.click()
    

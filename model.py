from initialize import *
from user_input import *

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

driver.get("https://release.gensom.sharajman.com/model")

driver.find_element(By.XPATH, "//div[@ngbtooltip='Add Model']").click()

#make dropdown
make_dropdown = driver.find_element(By.ID, "make")
select_make = Select(make_dropdown)
select_make.select_by_visible_text(make)

#category dropdown
category_dropdown = driver.find_element(By.ID, "category")
select_category = Select (category_dropdown)
select_category.select_by_visible_text(category)

#sub category dropdown
sub_category_dropdown = driver.find_element(By.ID, "subCategory")
select_sub_category = Select(sub_category_dropdown)
select_sub_category.select_by_visible_text(sub_category)

#enter model
driver.find_element(By.ID, "model").send_keys(model)

driver.find_element(By.XPATH, "//button[text()='Save']").click()

wait_toaster = WebDriverWait(driver, 10)
toaster = wait_toaster.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f" {toaster.text}")
toaster.click()




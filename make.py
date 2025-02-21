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

driver.get("https://release.gensom.sharajman.com/make")

add_make_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']")))
add_make_button.click()

make_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Make Here']")))
make_input.send_keys(make)

driver.find_element(By.XPATH, "//button[text()='Save']").click()

wait_toaster = WebDriverWait(driver, 10)
toaster = wait_toaster.until(EC.visibility_of_element_located((By.ID, "toast-container")))
print(f" {toaster.text}")
toaster.click()






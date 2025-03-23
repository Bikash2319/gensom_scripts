from initialize import *
import pandas as pd
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#setup
chrome_options = Options()
service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

#login
driver.get("https://release.gensom.sharajman.com/login")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash"))
driver.get("https://release.gensom.sharajman.com/plant-management/99/edit-plant")

Logger = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()='Data Logger Details']")))
Logger.click()

add_logger = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//button[text()=' Add Logger ']")))
add_logger.click()

time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Logger No']").send_keys("Logger 1")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Block Name']").send_keys("Block 1")

make_dd = Select(wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "make_id"))))
make_dd.select_by_visible_text("magamic")
time.sleep(1)
model_dd = wait.until(EC.element_to_be_clickable(driver.find_element(
By.CSS_SELECTOR, "[bindvalue='model_id']"
)))

actions = ActionChains(driver)
actions.click(model_dd).send_keys('model1').send_keys(Keys.ENTER).perform()

connectivity = Select(driver.find_element(By.ID, "internet_connectivity"))
connectivity.select_by_visible_text("Wi-fi")

dev_num = random.randint(10000, 99999)
driver.find_element(By.ID, "device_serial_no").send_keys(dev_num)

driver.find_element(By.ID, "folder_path_to_ftp").send_keys("D:\ftp\logger")

wms = Select(driver.find_element(By.ID,"wms_available"))
wms.select_by_visible_text("Yes")

plant = Select(driver.find_element(By.ID, "plant_curlainment"))
plant.select_by_visible_text("Yes")

driver.find_element(By.XPATH, "//button[text()='Submit']").click()
driver.find_element(By.XPATH("//button[text()= ' Cancel ']")).click()
print(f"{plant_name} and data logger added")


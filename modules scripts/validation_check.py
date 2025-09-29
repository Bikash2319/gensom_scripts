import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


#setup
chrome_options = Options()
service = Service(executable_path=r"C:\\Program Files\\Python313\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://release.gensom.sharajman.com/login")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")   

driver.get("https://release.gensom.sharajman.com/manage-users/users-details?action=add-user")
user_inputs = [
("abc123", True), ("123abc", True), ("a1", True), ("abc", False), ("123", False), ("!@#123", False), ("!@#abc", False), ("", False)
]

for value, should_pass in user_inputs:
    
    #time.sleep(1)
    webelement = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='identity_number']")))
    #webelement = driver.find_element((By.XPATH, "//input[@formcontrolname='identity_number']"))
    #webelement = driver.find_element(By.ID, "identity_number")
    #webelement.clear()
    webelement.send_keys(value)
    webelement.send_keys(Keys.TAB)

    time.sleep(1)

    try:
        error_element = driver.find_element(By.XPATH, "//label[text()='Identity No ']/following::span[contains(@class, 'ng-star-inserted')]")
        is_valid = error_element.text == ""
    except NoSuchElementException:
        is_valid = True  # If no error appears, assume valid

    result = "PASS" if is_valid == should_pass else "FAIL"
    print(f"Input: '{value}' | Expected: {should_pass} | Result: {is_valid} | Test: {result}")


    #time.sleep(2)

# driver.quit()
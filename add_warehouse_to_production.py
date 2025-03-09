from initialize import *
import pandas as pd

chrome_options = Options()
service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://release.gensom.sharajman.com/login")
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiaWthc2guc2Fob29Ac2hhcmFqbWFuLmNvbSIsImxvZ2luX2lkIjo0LCJ1c2VyX2lkIjo0LCJ1c2VyX3R5cGUiOiJPJk0gVEVBTSIsImV4cCI6MTc0MTM3MjkwNX0.uUP90DHXEetKT8jsZUwBslUedzb1pZ8tPLlZXZJJU3s"
# driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
driver.find_element(By.XPATH, "//button[text()='Login ']").click()
print("Login Successful")
wait = WebDriverWait(driver, 10)

driver.get("https://release.gensom.sharajman.com/warehouse")

file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, sheet_name="warehouse", engine='openpyxl')

# Convert to list of dictionaries
data_list = df.to_dict(orient="records")

for item in data_list:
    time.sleep(2)
    add_warehouse_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Warehouse']")))
    add_warehouse_button.click()
    print("Add warehouse button clicked")

    select_warehouse_type = Select(driver.find_element(By.ID, "warehouse_type"))
    select_warehouse_type.select_by_visible_text("INTERNAL")

    w_name = item.get("warehouse_name",)
    driver.find_element(By.ID,"warehouse_name").send_keys(w_name)
    
    country = Select(driver.find_element(By.ID, "country"))
    country.select_by_value("1")
    
    w_city = item.get("site_address")
    driver.find_element(By.ID, "city").send_keys(w_city)
    
    warehouse_address = item.get("site_address")
    driver.find_element(By.ID, "warehouse_address").send_keys(warehouse_address)

    try:
        init.save(driver)
        toaster = wait.until(EC.visibility_of_element_located((By.ID, "toast-container")))
        print(f"Toaster message: {toaster.text}")
        toaster.click()
        driver.find_element(By.XPATH, "//button[text()=' Back ']").click()

        # If already exists, cancel
        if toaster.text == " This Warehouse already exists ":
            init.cancel(driver)
            toaster.click()

    except Exception as e:
        print("Error:", e)
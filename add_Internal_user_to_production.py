from initialize import *

#setup
chrome_options = Options()
service = Service(executable_path=r"C:\Users\Bikash Chandra Sahoo\AppData\Local\Programs\Python\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# #login
# driver.get("https://release.gensom.sharajman.com/login")
# driver.find_element(By.ID, "floatingInputValue").send_keys("bikash.sahoo@sharajman.com")
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Admin@1234")
# driver.find_element(By.XPATH, "//button[text()='Login ']").click()
# print("Login Successful")
# wait.until(EC.url_to_be("https://release.gensom.sharajman.com/dash"))


#Inject token for authentication
driver.get("https://refex.gensomerp.com/")
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2hpc2gua0BzaGFyYWptYW4uY29tIiwibG9naW5faWQiOjMsInVzZXJfaWQiOjMsInVzZXJfdHlwZSI6Ik8mTSBURUFNIiwiZXhwIjoxNzQzNjIwODg0fQ.DHPJttVM3056PynPO1uBv-VSLvmGclZEz7OEc7aC9CE"
driver.execute_script(f"window.localStorage.setItem('token', '{token}');")
print("Login Successful")


file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
df = pd.read_excel(file_path, "inv")

data_list = df.to_dict(orient="records")

for item in data_list:
    driver.get("https://refex.gensomerp.com/manage-users")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//div[@ngbtooltip='Add User']").click()
    f_name = item.get("first_name")
    first_name = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//input[@formcontrolname='first_name']")))
    first_name.send_keys(f_name)
    print(first_name)
    time.sleep(0.5)

    l_name = item.get("last_name")
    last_name = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//input[@formcontrolname='last_name']")))
    if pd.isna(l_name) or l_name.strip() == "":
        last_name.send_keys(f_name)
    else:
        last_name.send_keys(l_name)

    email = item.get("email")
    email_field = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//input[@formcontrolname='email']")))
    email_field.send_keys(email)
    time.sleep(0.5)

    phone_number = item.get("mobile")
    ph_no = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//input[@formcontrolname='contact_number']")))
    ph_no.send_keys(f'+91{phone_number}')
    time.sleep(0.5)

    department_dd = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='department_id']"))
    department_dd.select_by_visible_text("Operations")
    time.sleep(0.5)

    time.sleep(1)
    designation_dd = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='designation_id']"))
    designation_dd.select_by_visible_text("Assistant Manager")
    time.sleep(0.5)

    user_type = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='userType']"))
    user_type.select_by_visible_text("SITE TEAM")
    time.sleep(0.5)

    id_num = driver.find_element(By.XPATH, "//input[@formcontrolname='identity_number']")
    characters = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"))
    random_identity = ''.join(np.random.choice(characters, 9))
    id_num.send_keys(random_identity)
    time.sleep(0.5)

    project_dd = driver.find_element(By.XPATH, "//ng-select//div[@class='ng-select-container']")
    project_dd.click()
    time.sleep(0.5)

    project_option = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//ng-dropdown-panel//div[contains(@class, 'ng-option') and span[text()='AIR JODHPUR']]")))
    project_option.click()
    time.sleep(0.5)

    enrollment_dd = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='enrollment']"))
    enrollment_dd.select_by_visible_text("INTERNAL")
    time.sleep(0.5)

    role_dd = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='role_type']"))
    role_dd.select_by_visible_text("TECHNICIAN")
    time.sleep(0.5)

    email_checkbox = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//input[@formcontrolname='isLoginAccessRequired']")))
    email_checkbox.click()
    time.sleep(0.5)

    save_button =  wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text()= 'Save']")))
    save_button.click()








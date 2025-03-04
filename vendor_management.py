from initialize import *
from user_input import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver , wait = init.init_login()

side_bar = driver.find_element(By.XPATH, "//aside[1]//ng-scrollbar//div")
management_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Management ')]")
side_bar.click()
management_menu.click()
driver.find_element(By.XPATH, "//a[@href='/vendor-managment']").click()

class vendor:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
    def add_new_vendor(self, vendor_name, contact_person, vendor_type, landline_number, contact_number, 
                   vendor_email_id, category, sub_category, comm_add, comm_state, 
                   same_as_billing_add, bill_add, bill_state):   
        add_vendor_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Vendor']")))
        add_vendor_button.click()
        print("Add vendor button clicked")

        self.driver.find_element(By.ID, "name").send_keys(vendor_name)
        self.driver.find_element(By.ID, "contactPerson").send_keys(contact_person)
        select_vType = Select(driver.find_element(By.ID, "vType"))
        select_vType.select_by_visible_text(vendor_type)

        self.driver.find_element(By.ID, "ldNo").send_keys(landline_number)
        self.driver.find_element(By.ID,"contactNumber").send_keys(contact_number)
        self.driver.find_element(By.ID, "email").send_keys(vendor_email_id)

        select_category = Select(driver.find_element(By.ID, "Classification"))
        select_category.select_by_visible_text(category)

        select_subcat = Select(driver.find_element(By.ID, "subclassification"))
        select_subcat.select_by_visible_text(sub_category)

        self.driver.find_element(By.ID, "communicationAddress").send_keys(comm_add)
        select_comm_country = Select(driver.find_element(By.ID, "country"))
        select_comm_country.select_by_value("1")

        select_comm_state = Select(driver.find_element(By.ID, "state"))
        select_comm_state.select_by_visible_text(comm_state)

        if(same_as_billing_add == 1):
            self.driver.find_element(By.ID, "sameAsBilling").click()
        else:
            self.driver.find_element(By.ID, "billingAddress").send_keys(bill_add)
            select_bill_country = Select(driver.find_element(By.ID, "billingCountry"))
            select_bill_country.select_by_value("1")
            select_bill_state = Select(driver.find_element(By.ID, "billingstate"))
            select_bill_state.select_by_visible_text(bill_state)


        dropdown_xpath = "//div[contains(@class, 'ng-select-container')]"
        dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
        dropdown.click()

        # Wait and select "Battery Setup"
        battery_setup_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Battery Setup']]"
        battery_setup =self. wait.until(EC.element_to_be_clickable((By.XPATH, battery_setup_xpath)))
        battery_setup.click()

        dropdown.click()
        # Wait and select "Oil Filtration"
        oil_filtration_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Oil Filtration']]"
        oil_filtration = self.wait.until(EC.element_to_be_clickable((By.XPATH, oil_filtration_xpath)))
        oil_filtration.click()

        dropdown.click()
        # Wait and select "Cable Configuration"
        Cable_Configuration_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Cable Configuration']]"
        Cable_Configuration = self.wait.until(EC.element_to_be_clickable((By.XPATH, Cable_Configuration_xpath)))
        Cable_Configuration.click()

        init.save(self.driver)
        
        print("Vendor added successfully!")


from initialize import *
from user_input import *

driver , wait = init.init_login()

driver.get("https://release.gensom.sharajman.com/vendor-managment")
class vendor:
    def add_new_vendor():   
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


        activity_tag_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ng-select-container')]")))
        activity_tag_dropdown.click()

        # Wait and select "Battery Setup"
        battery_setup_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Battery Setup']]"
        battery_setup = wait.until(EC.element_to_be_clickable((By.XPATH, battery_setup_xpath)))
        battery_setup.click()

        activity_tag_dropdown.click()
        # Wait and select "Oil Filtration"
        oil_filtration_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Oil Filtration']]"
        oil_filtration = wait.until(EC.element_to_be_clickable((By.XPATH, oil_filtration_xpath)))
        oil_filtration.click()

        activity_tag_dropdown.click()
        # Wait and select "Cable Configuration"
        Cable_Configuration_xpath = "//ng-dropdown-panel//div[contains(@class,'ng-option') and span[text()='Cable Configuration']]"
        Cable_Configuration = wait.until(EC.element_to_be_clickable((By.XPATH, Cable_Configuration_xpath)))
        Cable_Configuration.click()

        init.save(driver)
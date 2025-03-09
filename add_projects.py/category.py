from functions import *

def add_new_category():   
     
    side_bar = driver.find_element(By.XPATH, "//aside[1]//ng-scrollbar//div")
    master_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Master ')]")
    actions = ActionChains(driver)
    actions.move_to_element(side_bar).click().perform()
    actions.move_to_element(master_menu).click().perform()
    
    add_category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Category']")))
    add_category_button.click()

    add_category = wait.until(EC.visibility_of_element_located((By.ID, "catType")))
    add_category.send_keys(category)

    gensom.save(wait)
    gensom.toaster(wait)    
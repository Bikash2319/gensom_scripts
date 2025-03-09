from functions import *

print(variable.head())

def add_new_make():
    make = variable.loc[0, 'Make Name']
    side_bar = driver.find_element(By.XPATH, "//aside[1]//ng-scrollbar//div")
    master_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Master ')]")
    
    actions.move_to_element(side_bar).click#().perform()
    actions.move_to_element(master_menu).click().perform()

    driver.find_element(By.XPATH, "//a[@href='/make']").click()
    print('Make master clicked')

    add_make_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']")))
    add_make_button.click()

    make_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Make Here']")))
    make_input.send_keys(make)

    gensom.save(wait)
    gensom.toaster(wait)    
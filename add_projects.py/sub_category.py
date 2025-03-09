from functions import *

def add_new_subCat():
    file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
    variable = pd.read_excel(file_path, engine='openpyxl')
    
    category = variable.loc[1, 'Category Name']
    sub_category = variable.loc[2, 'Sub Category Name']
    
    side_bar = driver.find_element(By.XPATH, "//aside[1]//ng-scrollbar//div")
    master_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Master ')]")
    actions.move_to_element(side_bar).click().perform()
    actions.move_to_element(master_menu).click().perform()
    
    driver.find_element(By.XPATH, "//div[@ngbtooltip='Add SubCategory']").click()

    cat_dropdown = driver.find_element(By.ID, "catType")
    select_category = Select(cat_dropdown)
    select_category.select_by_visible_text(category)

    driver.find_element(By.ID, "subCat").send_keys(sub_category)

    driver.find_element(By.ID, "recordlevel").click()
    driver.find_element(By.ID, "serialnumber").click()
    driver.find_element(By.ID, "tilt").click()
    driver.find_element(By.ID, "mounting").click()

    gensom.save(driver)  
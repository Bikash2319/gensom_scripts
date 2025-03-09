from functions import *
import category
import make
import sub_category


def add_new_model():
    file_path = "D:\\GenSOM Variables\\GenSOM ERP Variables.xlsx"
    variable = pd.read_excel(file_path, engine='openpyxl')
    model = variable.loc[4, 'Model Name']
    
    side_bar = driver.find_element(By.XPATH, "//aside[1]//ng-scrollbar//div")
    master_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Master ')]")
    actions.move_to_element(side_bar).click().perform()
    actions.move_to_element(master_menu).click().perform()
    
    driver.find_element(By.XPATH, "//div[@ngbtooltip='Add Model']").click()

    #make dropdown
    make_dropdown = driver.find_element(By.ID, "make")
    select_make = Select(make_dropdown)
    select_make.select_by_visible_text(make)

    #category dropdown
    category_dropdown = driver.find_element(By.ID, "category")
    select_category = Select (category_dropdown)
    select_category.select_by_visible_text(category)

    #sub category dropdown
    sub_category_dropdown = driver.find_element(By.ID, "subCategory")
    select_sub_category = Select(sub_category_dropdown)
    select_sub_category.select_by_visible_text(sub_category)

    #enter model
    driver.find_element(By.ID, "model").send_keys(model) 
    
    gensom.save(driver)
    gensom.toaster(wait)   
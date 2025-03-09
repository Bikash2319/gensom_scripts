from functions import *
import pandas as pd
import make
import category

driver , wait = gensom.gensom_login()
management_menu = driver.find_element(By.XPATH, "//aside[1]//nav/ul/li/a/span[contains(text(), 'Management ')]")

make.add_make_button()
category.add_new_category()








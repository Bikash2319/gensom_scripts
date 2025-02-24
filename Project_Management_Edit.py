from initialize import *
from user_input import *

driver , wait = init.init_login()

driver.get("https://release.gensom.sharajman.com/plant-management")

driver.find_element(By.XPATH, "(//*[contains(@class,'feather-edit')])[1]").click()
time.sleep(3)
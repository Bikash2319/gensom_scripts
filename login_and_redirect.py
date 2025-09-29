import time
from selenium.webdriver.support import expected_conditions as ec
from login_file import login, setup_driver

driver, wait = setup_driver()
domain = "https://refex.dev.gensom.sharajman.com"

time.sleep(10)

login(driver, domain)
time.sleep(0.5)
driver.get(f"{domain}/make")
wait.until(ec.url_contains("make"))
print("make")
driver.get(f"{domain}/model")
time.sleep(0.5)
driver.get(f"{domain}/activity-master")
time.sleep(0.5)
driver.get(f"{domain}/category-master")
time.sleep(0.5)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
service = Service(executable_path=r"C:\\Program Files\\Python\\Scripts\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

# time.sleep(10)


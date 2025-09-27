from selenium import webdriver
from initialize import *


chrome_options = Options()
service = Service(executable_path=r"C:\\Program Files\\Python\\Scripts\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)


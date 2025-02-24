from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 



chrome_options = Options()
service = Service(executable_path="C:\Program Files\Python313\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


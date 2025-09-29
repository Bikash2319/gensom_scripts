import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from login_file import login

driver = webdriver.Chrome()
url = "https://refex.dev.gensomerp.com"

login(driver, url)

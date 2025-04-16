from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Category:

    def __init__(self, driver, wait):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)


        
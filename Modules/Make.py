from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
#from webelements import *



class Make:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_make_module(self):
        self.driver.get("https://release.gensom.sharajman.com/make")

    def click_on_add_make_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@ngbtooltip='Add Make']"))).click()

    def enter_make(self):
       make_name = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='make_name']")))
       make_name.send_keys("Testing Make")

    def click_on_save_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Save']"))).click()

    def verify_error_message_of_make_field(self):
        actual_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='make_name']/following::span"))).text
        expected_message = 'This field is required.'
        assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'" 

    def click_on_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Cancel']"))).click()

    

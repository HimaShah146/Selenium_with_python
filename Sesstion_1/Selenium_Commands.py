import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

#Application Commands
title=print(driver.title)       #nopCommerce demo store. Home page title
current_url=print(driver.current_url)       #https://demo.nopcommerce.com/
page_source=print(driver.page_source)


#Conditianal Commands

driver.find_element(By.XPATH,"(//li)[1]").click()
print(driver.find_element(By.XPATH,"(//input[@id='FirstName'])[1]").is_displayed())
print(driver.find_element(By.XPATH,"//input[@id='LastName']").is_enabled())
#Before selecting the radio button
print(driver.find_element(By.XPATH,"//input[@id='gender-female']").is_selected())
#After selecting the radio button
driver.find_element(By.XPATH,"//input[@id='gender-female']").click()
print(driver.find_element(By.XPATH,"//input[@id='gender-female']").is_selected())






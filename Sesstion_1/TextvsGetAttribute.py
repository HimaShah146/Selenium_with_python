import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
vstore = driver.find_element(By.XPATH,"//input[@id='Email']")
vstore.clear()
vstore.send_keys("abc@gmail.com")
print(vstore.text)
print(vstore.get_attribute("value"))
print(vstore.get_attribute('type'))
vstore1 = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print(vstore1.text)
print(vstore1.get_attribute("value"))
print(vstore1.get_attribute('type'))
time.sleep(5)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
time.sleep(3)
print(alert.text)
alert.send_keys("Welcome to Selenium")
alert.accept()  
time.sleep(3)
msg = driver.find_element(By.ID,"result").text
print(msg)
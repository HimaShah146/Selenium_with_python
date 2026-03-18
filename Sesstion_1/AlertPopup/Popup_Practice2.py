from selenium import webdriver
from selenium.webdriver.common.by import By     
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
print(driver.find_element(By.ID,"result").text)

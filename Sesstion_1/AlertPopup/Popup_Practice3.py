from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
driver.maximize_window()

#Inject the username and password into your URL
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
msg = driver.find_element(By.XPATH,"//p").text
print(msg)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time     

driver = webdriver.Chrome()
driver.maximize_window()        
driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

#How to go inner frames using web element of the frame

#Outer frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']"))

#inner frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']"))
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome to Selenium")
time.sleep(3)
#driver.switch_to.parent_frame() #To go back to outer frame
driver.switch_to.default_content() #To go back to main page

driver.find_element(By.XPATH,"//a[normalize-space()='Home']").click()
print("\nTest Completed\n\n")

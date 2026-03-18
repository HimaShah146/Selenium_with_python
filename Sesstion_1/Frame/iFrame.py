from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://vinothqaacademy.com/iframe/")

#How to witch between multiple frames using name of the frame
driver.switch_to.frame("employeetable") 
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[3]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[2]/tbody[1]/tr[1]/td[1]/input[1]").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("popuppage")
driver.find_element(By.XPATH,"//button[normalize-space()='Alert Box']").click()
driver.switch_to.alert.accept()
msg = driver.find_element(By.XPATH,"//p[@id='demotwo']").text
print(msg)
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("registeruser")
driver.find_element(By.XPATH,"//input[@id='vfb-5']").send_keys("Selenium")
time.sleep(3)
driver.switch_to.default_content()

driver.find_element(By.XPATH,"//div[@class='collapse navbar-collapse pull-right']//a[normalize-space()='Home']").click()

print("\nTest Completed\n\n")

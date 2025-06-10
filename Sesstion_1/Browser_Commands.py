import time
from idlelib.colorizer import prog_group_name_to_tag

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://saucelabs.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"(//div[@class='MuiStack-root css-j7qwjs'])[2]").click()
#driver.close()
time.sleep(10)
driver.find_element(By.XPATH,"(//button[normalize-space()='Sign in'])[1]").click()
time.sleep(5)
driver.quit()



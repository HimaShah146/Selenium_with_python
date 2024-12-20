#https://techbeamers.com/websites-to-practice-selenium-webdriver-online/#onlytesting-demo-site

#open browser (chrome, firefox, edge)
#open website ur (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
#enter username (Admin)
#enter password (admin123)
#capture the home page title actual output
#verify the expected output
#compare the actual and excepted result
# close the browser

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from se

#driver=webdriver.Chrome("C:\Decho "# Selenium_with_python" >> README.mdrivers\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(r"C:\Drivers\chromedriver-win64\chromedriver" )
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sagituce")
driver.find_element(By.ID,"login-button").click()

actual_output = driver.title
excepted_output = "Swag Labs"
if actual_output == excepted_output:
    print("Pass")
else:
    print("Fail")

driver.close()


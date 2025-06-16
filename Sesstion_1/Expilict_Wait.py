from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

#Declaring Explicitly wait
#Basic syntax:
mywait = WebDriverWait(driver,5)

#Exception handling using only one ignored_exception() :
#mywait=WebDriverWait(driver,10,ignored_exceptions=[Exception])

driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.find_element(By.ID,"btn-make-appointment").click()
driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID,"btn-login").click()
driver.find_element(By.XPATH,"//input[@id='chk_hospotal_readmission']").click()
value = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='chk_hospotal_readmission']")))

# value = mywait.until(EC.element_to_be_clickable((By.ID,"btn-login")))
#
print(value)


# mywait.until(EC.presence_of_element_located((By.XPATH,"(//div[@id='dismissible'])[55]")))

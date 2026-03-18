from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown = driver.find_element(By.ID,"dropdown")

# Using index number
# options = dropdown.find_elements(By.TAG_NAME,"option")
# print("Total options: ",len(options))   
# for option in options:
#     print(option.text)
# time.sleep(3)
# options[1].click() #Option 1
#time.sleep(3)

#Using value attribute
# dropdown.find_element(By.CSS_SELECTOR,"option[value='2']").click()
# optbyvalueattribute= dropdown.find_element(By.CSS_SELECTOR,"option[value='2']").text   
# print("Selected option: ",optbyvalueattribute )
#time.sleep(3)

#Using text
dropdown.find_element(By.XPATH,"//option[normalize-space(text()) = 'Option 1']").click()
time.sleep(3)
optbytextname = dropdown.find_element(By.XPATH,"//option[normalize-space(text()) = 'Option 1']").text   
print("Selected option: ",optbytextname)



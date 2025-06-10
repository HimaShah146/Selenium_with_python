import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
msg = driver.find_element(By.XPATH,"//a[text()='GCM Capital Advisors']/self::a").text # GCM Capital Advisors

msg1 = driver.find_element(By.XPATH,"(//tr)[10]/descendant::td[3]").text #6.97

msg2 = driver.find_element(By.XPATH,"//a[text()='GCM Capital Advisors']/ancestor:: tr").text #GCM Capital Advisors M 6.97 8.00 + 14.78 Buy  |  Sell

msg3 = driver.find_element(By.XPATH,"//a[text()='GCM Capital Advisors']/ancestor:: tr/child::td[5]").text #+ 14.78

msg4 = driver.find_element(By.XPATH,"//a[text()='GCM Capital Advisors']/ancestor:: tr/preceding-sibling::tr[1]").text #Ajcon Global Service X 72.21 83.75 + 15.98 Buy  |  Sell

msg5 = driver.find_elements(By.XPATH,"//a[text()='GCM Capital Advisors']/ancestor:: tr/following-sibling::tr") # 2021

msg6 = driver.find_element(By.XPATH,"//a[text()='GCM Capital Advisors']/ancestor:: tr/following-sibling::tr").text #  Hubtown B 181.20 206.90 + 14.18 Buy  |  Sell

msg7 = driver.find_element(By.XPATH,"//a[text()='GCM Capital Advisors']/parent::td").text

msg8 = driver.find_elements(By.XPATH,"//a[text()='GCM Capital Advisors']/following::tr")

print("Self Locator: ",msg,"\nDescendant: ",msg1,"\nAncestor: ",msg2,"\nChild: ",msg3,"\nPreceding Sibling: ",msg4,"\nFollowing Sibling: ",msg6,"\nParent: ",msg7 )
print(len(msg5))
print(len(msg8))
time.sleep(3)
driver.get("https://money.rediff.com/gainers/bse/daily/groupz")
v= driver.find_element(By.XPATH,"//a[text()='HDIL']/following::tr[2]").text
print(v)


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
msg = driver.find_element(By.XPATH,"//a[text()='GCM Capital Advisors']/self::a").text
msg1 = driver.find_element(By.XPATH,"(//tr)[10]/descendant::td[3]").text
msg2 = driver.find_element(By.XPATH,"//a[normalize-space()='GCM Capital Advisors']/ancestor:: tr").text
msg3 = driver.find_element(By.XPATH,"//a[normalize-space()='GCM Capital Advisors']/ancestor:: tr/child::td[5]").text
msg4 = driver.find_element(By.XPATH,"//a[normalize-space()='GCM Capital Advisors']/ancestor:: tr/preceding-sibling::tr[1]").text
msg5 = driver.find_elements(By.XPATH,"//a[normalize-space()='GCM Capital Advisors']/ancestor:: tr/following-sibling::tr")
msg6 = driver.find_element(By.XPATH,"//a[normalize-space()='GCM Capital Advisors']/ancestor:: tr/following-sibling::tr").text
print("Self Locator: ",msg,"\nDescendant: ",msg1,"\nAncestor: ",msg2,"\nChild: ",msg3,"\nPreceding Sibling: ",msg4,"\nFollowing Sibling: ",msg6)
print(len(msg5))



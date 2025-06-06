from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
title=print(driver.title)       #nopCommerce demo store. Home page title
current_url=print(driver.current_url)       #https://demo.nopcommerce.com/
page_source=print(driver.page_source)

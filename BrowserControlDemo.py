from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/Downloads/QSpiders/chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//a[text()='flights']").click()
driver.find_element_by_xpath("//a[text()='hotels']").click()
driver.back()
driver.forward()
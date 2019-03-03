# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/Downloads/QSpiders/chromedriver.exe")
# driver.get("https://phptravels.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# first_window_id = driver.current_window_handle
# print(first_window_id)
#
# # before going to the next step we have to import the time packages
# time.sleep(15)
# driver.find_element_by_xpath("//span[text()='Login']").click()
#
# # Now we eed to find the window id`s of multiple windows
# multiple_window_id = driver.window_handles
# print(multiple_window_id)
# print(type(multiple_window_id))
#
# # Now we need to switch between the Parent window to the child window
# # We understood that the window id`s will be saved as in the list format. and Swichig can be done using the index of that list.
#
# print(multiple_window_id[1])
#
# driver.switch_to.window(multiple_window_id[1])
#
# # Sometimes the chile window will not be loaded by itself, so we need to refresh the page. Do do that we have to write code for refreshing that chile window
# driver.refresh()
#
# # Now we reached in the child window and we can do any oparations in that window
# driver.find_element_by_id("inputEmail").send_keys("TestName")

# the above work we can automate by putting that in the for loop


# -----------------------------------------------------------------------------------------------------------

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/Downloads/QSpiders/chromedriver.exe")
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(10)
first_window_id = driver.current_window_handle
print(first_window_id)
current_window_id = driver.current_window_handle
time.sleep(15)
driver.find_element_by_xpath("//span[text()='Login']").click()
multiple_window_id = driver.window_handles
# driver.refresh()   -> Never to user this comment as updated by Harish -> Even though the code will work it is not recommented
# Reason We are
for id in multiple_window_id:
    if (current_window_id != id):
        driver.switch_to.window(id)
        # time.sleep(5)
        # driver.refresh()
        driver.find_element_by_id("inputEmail").send_keys("TestName")

# driver.close()
driver.quit()
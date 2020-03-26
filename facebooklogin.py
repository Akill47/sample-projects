from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\Akhil\PycharmProjects\automation\drivers\chromedriver_win32 (1)\chromedriver.exe")
driver.set_page_load_timeout(5)
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("akhil.rocking10@gmail.com")
driver.find_element_by_name("pass").send_keys("cherryakhil")
driver.find_element_by_id("u_0_b").click()
driver.find_element_by_id("userNavigationLabel").click()
driver.find_element_by_class_name("_54nh").click()
time.sleep(4)
driver.quit()
print("script successfully executed")
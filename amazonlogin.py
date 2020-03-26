from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"C:\Users\Akhil\PycharmProjects\automation\drivers\chromedriver_win32 (1)\chromedriver.exe")
driver.set_page_load_timeout(5)
driver.get("https://www.amazon.in/")
driver.find_element_by_id("nav-link-accountList").send_keys(Keys.ENTER)
driver.find_element_by_class_name("nav-action-inner").click()
driver.find_element_by_name("email").send_keys("akhil.rocking10@gmail.com")
driver.find_element_by_class_name("a-button-input").send_keys(Keys.ENTER)
driver.find_element_by_name("password").send_keys("8686500356A")
driver.find_element_by_class_name("a-button-input").send_keys(Keys.ENTER)
driver.find_element_by_name("field-keywords").send_keys("playstation 4")
driver.find_element_by_class_name("nav-input").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
print("script successfully executed")
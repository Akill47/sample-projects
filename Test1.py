from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Akhil\PycharmProjects\automation\drivers\chromedriver_win32 (1)\chromedriver.exe")
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get("https://www.youtube.com/?gl=IN")
driver.find_element_by_name("search_query").send_keys('hello')
driver.find_element_by_id("search-icon-legacy").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
print("script successfully executed")
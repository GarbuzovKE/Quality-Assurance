from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


def add_comment(driver:webdriver):
    # 1
    driver.get("https://practice.automationtesting.in/")
    # 2
    driver.execute_script("window.scrollBy(0, 600);")
    # 3
    driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/selenium-ruby/']").click()
    # 4
    driver.find_element_by_css_selector("[href='#tab-reviews']").click()
    # 5
    driver.find_element_by_class_name("star-5").click()
    # 6
    driver.find_element_by_id("comment").send_keys("Nice book!")
    # 7
    driver.find_element_by_id("author").send_keys("Pedro")
    # 8
    driver.find_element_by_id("email").send_keys("amazingemaildude@omg.com")
    # 9
    driver.find_element_by_id("submit").click()
    print("Add comment pass")


path_to_extension = r'C:\Users\kirkr\AppData\Local\Google\Chrome\User Data\Default\Extensions\cfhdojbkjhnklbpkdaibdccddilifddb\3.17.1_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
_driver = webdriver.Chrome(options=chrome_options)
_driver.create_options()
time.sleep(10)
# driver.maximize_window()
first_browser_tab = _driver.window_handles[0]
_driver.switch_to.window(first_browser_tab)
_driver.implicitly_wait(5)
_driver.set_page_load_timeout(5)
add_comment(driver=_driver)
_driver.quit()

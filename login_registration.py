from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


def registration(driver: webdriver, email, password):
    # 1
    driver.get("https://practice.automationtesting.in/")
    # 2
    driver.find_element_by_link_text("My Account").click()
    # 3
    driver.find_element_by_id("reg_email").send_keys(email)
    # 4
    driver.find_element_by_id("reg_password").send_keys(password)
    # 5
    driver.find_element_by_name("register").click()
    print("Registration pass")
    # time.sleep(10)


def login(driver: webdriver, email, password):
    # 1
    driver.get("https://practice.automationtesting.in/")
    # 2
    driver.find_element_by_link_text("My Account").click()
    # 3
    driver.find_element_by_id("username").send_keys(email)
    # 4
    driver.find_element_by_id("password").send_keys(password)
    # 5
    driver.find_element_by_name("login").click()
    # 6
    logout_status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
    print("Login pass")
    # time.sleep(10)


if __name__ == "__main__":
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
    email = "amazingemaildude@omg.com"
    password = "!@#Amazing_password_dude"
    _driver.set_page_load_timeout(5)

    # registration(driver, email, password)
    login(driver=_driver, email=email, password=password)

    _driver.quit()
    print("Success")

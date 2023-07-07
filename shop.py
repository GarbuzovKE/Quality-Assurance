from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from login_registration import login
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException


def show_item_page(driver: webdriver):
    # 3
    driver.find_element_by_link_text("Shop").click()
    # 4
    driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/html5-forms/']").click()
    # 5
    assert driver.find_element_by_css_selector(".summary>h1").text == "HTML5 Forms", "Book title is not 'HTML5 Forms'"
    print("Show item page pass")
    time.sleep(10)


def check_items_amount(driver: webdriver):
    # 3
    driver.find_element_by_link_text("Shop").click()
    # 4
    driver.find_element_by_link_text("HTML").click()
    # 5
    html_items = driver.find_elements_by_class_name("wp-post-image")
    assert len(html_items) == 3, "Number of items on page is not 3"
    print("Check items amount pass")
    time.sleep(10)


def items_sort(driver: webdriver):
    # 3
    driver.find_element_by_link_text("Shop").click()
    # 4
    assert driver.find_element_by_css_selector('.orderby>[value="menu_order"]').get_attribute(
        'selected'), "Default sorting is not picked"
    # 5
    sorting = driver.find_element_by_tag_name('select')
    select_sorting = Select(sorting)
    select_sorting.select_by_visible_text("Sort by price: high to low")
    # 6
    sorting = driver.find_element_by_css_selector('.orderby>[value="price-desc"]')
    # 7
    assert sorting.text == "Sort by price: high to low", "Sort by price: high to low should be selected"
    print("Items sort pass")
    time.sleep(10)


def inspect_sale_check(driver: webdriver):
    # 3
    driver.find_element_by_link_text("Shop").click()
    # 4
    driver.find_element_by_css_selector("[alt='Android Quick Start Guide']").click()
    # 5
    book_prices = driver.find_elements_by_css_selector("p.price .amount")
    assert book_prices[0].text[1:] == "600.00", "Old price should be 650.00"
    # 6
    assert book_prices[1].text[1:] == "450.00", "New price should be 450.00"
    # 7 не понял что имеется ввиду под предпросмотром картинки
    book_img_check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[alt='Android Quick Start Guide']")))
    driver.find_element_by_css_selector("[alt='Android Quick Start Guide']").click()
    # 8
    close_btn_check = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_details>a")))
    driver.find_element_by_css_selector(".pp_details>a").click()
    print("Inspect sale pass")
    time.sleep(10)


def check_price_in_cart(driver: webdriver):
    # 1
    driver.get("https://practice.automationtesting.in/")
    # 2
    driver.find_element_by_link_text("Shop").click()
    # 3
    driver.find_element_by_css_selector("[data-product_id='182']").click()
    # 4
    WebDriverWait(driver, 2).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#wpmenucartli .cartcontents"), "1 Item"))
    assert driver.find_element_by_css_selector(
        "#wpmenucartli .cartcontents").text == "1 Item", "1 Item should be in a cart"
    assert driver.find_element_by_css_selector("#wpmenucartli .amount").text[1:] == "180.00", "Price should be 180.00"
    # 5
    driver.find_element_by_css_selector("#wpmenucartli>a").click()
    # 6
    subtotal_cart_check = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "₹180.00"))
    # 7
    total_cart_check = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "₹183.60"))
    print("Check price in cart pass")
    time.sleep(10)


def check_cart_activities(driver: webdriver):
    # 1
    driver.get("https://practice.automationtesting.in/")
    # 2
    driver.find_element_by_link_text("Shop").click()
    # 3
    driver.execute_script("window.scrollBy(0, 300);")
    driver.find_element_by_css_selector("[data-product_id='182']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("[data-product_id='180']").click()
    time.sleep(3)
    # 4
    driver.find_element_by_css_selector("#wpmenucartli>a").click()
    # 5
    time.sleep(2)
    driver.find_element_by_css_selector(".cart tbody .cart_item a").click()
    # 6
    driver.find_element_by_link_text("Undo?").click()
    # 7
    js_book_amount = driver.find_element_by_xpath("//*[@data-product_id='180']/../..//div[@class='quantity']/input")
    js_book_amount.clear()
    js_book_amount.send_keys("3")
    # 8
    driver.find_element_by_name("update_cart").click()
    # 9
    time.sleep(3)
    js_book_amount = driver.find_element_by_xpath("//*[@data-product_id='180']/../..//div[@class='quantity']/input")
    assert js_book_amount.get_attribute("value") == "3", "Quantity of JS books should be 3"
    # 10
    time.sleep(3)
    driver.find_element_by_name("apply_coupon").click()
    # 11
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Please enter a coupon code.')]")))
    print("Check cart activities pass")


def check_buy_item(driver: webdriver):
    # 1
    driver.get("https://practice.automationtesting.in/")
    # 2
    driver.find_element_by_link_text("Shop").click()
    driver.execute_script("window.scrollBy(0, 300);")
    # 3
    driver.find_element_by_css_selector("[data-product_id='182']").click()
    time.sleep(3)
    # 4
    driver.find_element_by_css_selector("#wpmenucartli>a").click()
    # 5
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")))
    driver.find_element_by_css_selector(".wc-proceed-to-checkout>a").click()
    # 6
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "billing_first_name")))
    driver.find_element_by_id("billing_first_name").send_keys("Pedro")
    driver.find_element_by_id("billing_last_name").send_keys("Alduare")
    driver.find_element_by_id("billing_email").send_keys(email)
    driver.find_element_by_id("billing_phone").send_keys("+72375678901")
    driver.find_element_by_id("s2id_billing_country").click()
    driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
    time.sleep(3)
    driver.find_element_by_css_selector("#select2-results-1>li").click()
    driver.find_element_by_id("billing_address_1").send_keys("Leninskiy av. 2")
    driver.find_element_by_id("billing_city").send_keys("Saint-Petersburg")
    driver.find_element_by_id("billing_state").send_keys("Saint-Petersburg")
    driver.find_element_by_id("billing_postcode").send_keys("768125")
    # 7
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(3)
    driver.find_element_by_id("payment_method_cheque").click()
    # 8
    driver.find_element_by_id("place_order").click()
    # 9
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you. Your order has been received.')]")))
    # 10
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"))


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
    _driver.set_page_load_timeout(10)
    email = "amazingemaildude@omg.com"
    password = "!@#Amazing_password_dude"
    # login(_driver, email, password)
    # show_item_page(_driver)
    # check_items_amount(_driver)
    # items_sort(_driver)
    # inspect_sale_check(_driver)
    # check_price_in_cart(_driver)
    # check_cart_activities(_driver)
    check_buy_item(_driver)

    _driver.quit()
    print("Success")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.fixture
def driver():
    # create a webdriver instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # close the webdriver instance
    driver.quit()

def test_homepage(driver):
    # navigate to a webpage
    driver.get("https://www.thebeautifulcompany.co.uk/")

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "body > div > div:nth-child(1) > div.digi-overlay > div > svg > path:nth-child(1)"))
    # )
    #
    # pop_up = driver.find_element(By.CSS_SELECTOR, "body > div > div:nth-child(1) > div.digi-overlay > div > svg > path:nth-child(1)")
    # pop_up.click()
    #
    # # wait for the page to load
    # WebDriverWait(driver, 10)

    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(2)

# def test_product(driver):
#     # navigate to a webpage
#     driver.get("https://www.thebeautifulcompany.co.uk/")
#
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li.js-hover-delay.has-dropdown.wrap.open > div > div"))
#     )
#
#     platinum_wedding_ring = driver.find_element(By.CSS_SELECTOR, '#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li.js-hover-delay.has-dropdown.wrap.open > div > div > div > div.column.xlarge-9.padding-l8.padding-r0 > div > div:nth-child(1) > a')
#     platinum_wedding_ring.click()
#     time.sleep(5)
#
#     product_1 = driver.find_element(By.CSS_SELECTOR, '#product-grid > div:nth-child(1) > a > span.block.line-height-1pt4.margin-b5')
#     product_1.click()
#     time.sleep(2)
#
# def test_add_to_cart(driver):
#     # navigate to a webpage
#     driver.get("https://www.thebeautifulcompany.co.uk/")
#
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li.js-hover-delay.has-dropdown.wrap.open > div > div"))
#     )
#
#     platinum_wedding_ring = driver.find_element(By.CSS_SELECTOR, '#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li.js-hover-delay.has-dropdown.wrap.open > div > div > div > div.column.xlarge-9.padding-l8.padding-r0 > div > div:nth-child(1) > a')
#     platinum_wedding_ring.click()
#     time.sleep(5)
#
#     product_1 = driver.find_element(By.CSS_SELECTOR, '#product-grid > div:nth-child(1) > a > span.block.line-height-1pt4.margin-b5')
#     product_1.click()
#     time.sleep(2)
#
#     add_to_cart = driver.find_element(By.CSS_SELECTOR, '#add-to-cart')
#     add_to_cart.click()
#     time.sleep(5)

def test_basket(driver):
    # navigate to a webpage
    driver.get("https://www.thebeautifulcompany.co.uk/")

    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(2)

    submenu = driver.find_element(By.CSS_SELECTOR, "#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li:nth-child(1)")
    hover = ActionChains(driver).move_to_element(submenu)
    hover.perform()

    submenu_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li.js-hover-delay.has-dropdown.wrap.open > div > div"))
    )

    platinum_wedding_ring = driver.find_element(By.CSS_SELECTOR, '#header > div.background.colour-blue-grey-dark > div > div > nav > ul > li.js-hover-delay.has-dropdown.wrap.open > div > div > div > div.column.xlarge-9.padding-l8.padding-r0 > div > div:nth-child(1) > a')
    platinum_wedding_ring.click()
    time.sleep(5)

    product_1 = driver.find_element(By.CSS_SELECTOR, '#product-grid > div:nth-child(1) > a > span.block.line-height-1pt4.margin-b5')
    product_1.click()
    time.sleep(2)

    add_to_cart = driver.find_element(By.CSS_SELECTOR, '#add-to-cart')
    add_to_cart.click()
    time.sleep(5)

    basket = driver.find_element(By.CSS_SELECTOR, '#cart > a')
    basket.click()
    time.sleep(5)

    checkout = driver.find_element(By.CSS_SELECTOR, '#shop-cart > div.padding-b20 > div > div.column.medium-6.large-3.padding-l20-medium-only > a')
    checkout.click()
    time.sleep(5)

    guest_checkout = driver.find_element(By.CSS_SELECTOR, '#account > span:nth-child(3) > span.table-cell.vertical-top.width-100 > label')
    guest_checkout.click()
    time.sleep(5)

    guest_checkout_continue = driver.find_element(By.CSS_SELECTOR, '#account > button')
    guest_checkout_continue.click()
    time.sleep(5)

    first_name = driver.find_element(By.CSS_SELECTOR, '#firstname')
    first_name.send_keys('newtest')
    time.sleep(5)

    last_name = driver.find_element(By.CSS_SELECTOR, '#lastname')
    last_name.send_keys('chauhan')
    time.sleep(5)

    email = driver.find_element(By.CSS_SELECTOR, '#email')
    email.send_keys('test@gmail.com')
    time.sleep(5)

    telephone = driver.find_element(By.CSS_SELECTOR, '#telephone')
    telephone.send_keys('0000000000')
    time.sleep(5)

    address_1 = driver.find_element(By.CSS_SELECTOR, '#address_1')
    address_1.send_keys('sibfusihb')
    time.sleep(5)

    city = driver.find_element(By.CSS_SELECTOR, '#city')
    city.send_keys('dsgvdga')
    time.sleep(5)

    passcode = driver.find_element(By.CSS_SELECTOR, '#postcode-input')
    passcode.send_keys('RG52')
    time.sleep(5)

    region = driver.find_element(By.CSS_SELECTOR, '#zone_id')
    region.send_keys('Aberdeen')
    time.sleep(5)

    country = driver.find_element(By.CSS_SELECTOR, '#country_id')
    country.send_keys('United Kingdom')
    time.sleep(5)

    continue_guest = driver.find_element(By.CSS_SELECTOR, '#guest > div > div.table-cell.text-right > button')
    continue_guest.click()
    time.sleep(5)

    payment_selection = driver.find_element(By.CSS_SELECTOR, '#guest > fieldset.border-5.colour-grey-lightest.padding-b10.padding-b0-large-up.margin-t0.margin-b20.margin-b30-medium-up > div > div > div.payment-method.method-sagepay_v3.column.large-6.end.margin-b10.margin-b20-large-up > label > span > span:nth-child(2) > span')
    payment_selection.click()
    time.sleep(5)

    payment_button = driver.find_element(By.CSS_SELECTOR,'#guest > div > div.table-cell.text-right > button')
    payment_button.click()
    time.sleep(5)

    payment_confirm = driver.find_element(By.CSS_SELECTOR, '#checkout > div > div > button')
    payment_confirm.click()
    time.sleep(5)





    # shop-cart > div.padding-b20 > div > div.column.medium-6.large-3.padding-l20-medium-only > a








#
#     oneonone = driver.find_element(By.CSS_SELECTOR, '#menu-item-20088 > a:nth-child(1)')
#     oneonone.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-18730 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-18730 > a"))
#     )
#
#     groupsession = driver.find_element(By.CSS_SELECTOR, '#menu-item-20090 > a:nth-child(1)')
#     groupsession.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-18730 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-18730 > a"))
#     )
#
#     become_a_pro_member = driver.find_element(By.CSS_SELECTOR, '#menu-item-18442 > a:nth-child(1)')
#     become_a_pro_member.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-18730 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-18730 > a"))
#     )
#
#     summer_session_2023 = driver.find_element(By.CSS_SELECTOR, '#menu-item-24890 > a:nth-child(1)')
#     summer_session_2023.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
# def test_Blog(driver):
#     # navigate to a webpage
#     driver.get("https://oratoracademy.com/")
#
#
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".sgpb-popup-close-button-1"))
#     )
#
#     pop_up = driver.find_element(By.CSS_SELECTOR, ".sgpb-popup-close-button-1")
#     pop_up.click()
#
#     # find the navigation menu element and click on it
#     blog1 = driver.find_element(By.CSS_SELECTOR, "#menu-item-19560 > a:nth-child(1)")
#     blog1.click()
#
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#
# def test_Contact(driver):
#     # navigate to a webpage
#     driver.get("https://oratoracademy.com/")
#
#
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".sgpb-popup-close-button-1"))
#     )
#
#     pop_up = driver.find_element(By.CSS_SELECTOR, ".sgpb-popup-close-button-1")
#     pop_up.click()
#
#     # find the navigation menu element and click on it
#     contactus = driver.find_element(By.CSS_SELECTOR, "#menu-item-17340 > a:nth-child(1)")
#     contactus.click()
#
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
# def test_masteroratory(driver):
#     # navigate to a webpage
#     driver.get("https://oratoracademy.com/")
#
#
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".sgpb-popup-close-button-1"))
#     )
#
#     pop_up = driver.find_element(By.CSS_SELECTOR, ".sgpb-popup-close-button-1")
#     pop_up.click()
#
#     # wait for the page to load
#     WebDriverWait(driver, 10)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-21876 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-21876> a"))
#     )
#
#     public_speaking = driver.find_element(By.CSS_SELECTOR, '#menu-item-21879 > a:nth-child(1)')
#     public_speaking.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-21876 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-21876> a"))
#     )
#
#     stage_fear = driver.find_element(By.CSS_SELECTOR, '#menu-item-21880 > a:nth-child(1)')
#     stage_fear.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-21876 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-21876> a"))
#     )
#
#     communication_skill = driver.find_element(By.CSS_SELECTOR, '#menu-item-21878 > a:nth-child(1)')
#     communication_skill.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-21876 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-21876> a"))
#     )
#
#     business_story = driver.find_element(By.CSS_SELECTOR, '#menu-item-21877 > a:nth-child(1)')
#     business_story.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-21876 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-21876> a"))
#     )
#
#     interview_skill= driver.find_element(By.CSS_SELECTOR, '#menu-item-21898 > a:nth-child(1)')
#     interview_skill.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-21876 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-21876> a"))
#     )
#
#     personality_development = driver.find_element(By.CSS_SELECTOR, '#menu-item-21899 > a:nth-child(1)')
#     personality_development.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-21876 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-21876> a"))
#     )
#
#     presentation_skill = driver.find_element(By.CSS_SELECTOR, '#menu-item-21900 > a:nth-child(1)')
#     presentation_skill.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
# def test_resource(driver):
#     # navigate to a webpage
#     driver.get("https://oratoracademy.com/")
#
#
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".sgpb-popup-close-button-1"))
#     )
#
#     pop_up = driver.find_element(By.CSS_SELECTOR, ".sgpb-popup-close-button-1")
#     pop_up.click()
#
#     # wait for the page to load
#     WebDriverWait(driver, 10)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-24147 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-24147> a"))
#     )
#     submenu_new = driver.find_element(By.CSS_SELECTOR, "#menu-item-23069 > a:nth-child(1)")
#
#     hover2 = ActionChains(driver).move_to_element(submenu_new)
#     hover2.perform()
#
#     submenu2 = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#menu-item-23069> a"))
#     )
#
#
#     review = driver.find_element(By.XPATH, '/html/body/div[1]/div/header/div/div/div/section[2]/div/div/div[2]/div/div/div/div/nav/ul/li[4]/ul/li[1]/ul/li[1]/a')
#     review.click()
#     time.sleep(5)
#
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-24147 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-24147> a"))
#     )
#     submenu_new = driver.find_element(By.CSS_SELECTOR, "#menu-item-23069 > a:nth-child(1)")
#
#     hover2 = ActionChains(driver).move_to_element(submenu_new)
#     hover2.perform()
#
#     submenu2 = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#menu-item-23069> a"))
#     )
#
#     write_review = driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div/div/section[2]/div/div/div[2]/div/div/div/div/nav/ul/li[4]/ul/li[1]/ul/li[2]/a')
#     write_review.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)
#
#
#     submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-24147 > a:nth-child(1)")
#     hover = ActionChains(driver).move_to_element(submenu)
#     hover.perform()
#
#     submenu_items = WebDriverWait(driver, 10).until(
#         EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-24147> a"))
#     )
#
#     gallery = driver.find_element(By.CSS_SELECTOR, '#menu-item-18139 > a:nth-child(1)')
#     gallery.click()
#     time.sleep(5)
#     total_height = int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)


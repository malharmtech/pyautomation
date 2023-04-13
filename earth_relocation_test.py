import pytest
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_website(browser):
    browser.get('https://www.earthrelocation.com/')
    assert browser.title == "Moving Company Near Me | Moving Services Near Me | Movers Near Me | Earth Relocation"

def test_website1(browser):
    browser.get('https://www.earthrelocation.com/why-choose-us/')
    assert browser.title == "Why choose us for your move!"

def test_aboutus(browser):
    browser.get('https://www.earthrelocation.com/moving-to-scotland-from-us/')
    assert browser.title == "Moving To Scotland From US | Relocating To Scotland From US | Moving Company To Scotland From US"

# @pytest.fixture(scope='module')
# def browser():
#     driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
#     driver.maximize_window()
#     driver.get("https://www.earthrelocation.com/free-online-moving-quote/")
#     originaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_1_1")
#     originaddress.send_keys("sdfdz")
#     originstreetaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_1_3")
#     originstreetaddress.send_keys("abauihb")
#     originstateaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_1_4")
#     originstateaddress.send_keys("sagbsduvb")
#     originzipaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_1_5")
#     originzipaddress.send_keys("382345")
#     origincountry = driver.find_element(By.CSS_SELECTOR, "#input_16_1_6")
#     origincountry.send_keys("India")
#     destinationaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_2_1")
#     destinationaddress.send_keys("euvuavhfebv")
#     destinationstreetaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_2_3")
#     destinationstreetaddress.send_keys("lkjlhjjbnv")
#     destinationstateaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_2_4")
#     destinationstateaddress.send_keys("ojhbvgg")
#     destinationzipaddress = driver.find_element(By.CSS_SELECTOR, "#input_16_2_5")
#     destinationzipaddress.send_keys("382344")
#     destinationcountry = driver.find_element(By.CSS_SELECTOR, "#input_16_2_6")
#     destinationcountry.send_keys("Algeria")
#     fname = driver.find_element(By.CSS_SELECTOR, '#input_16_8')
#     time.sleep(2)
#     fname.send_keys("malhar")
#     lname = driver.find_element(By.CSS_SELECTOR, '#input_16_25')
#     time.sleep(2)
#     lname.send_keys("chauhan")
#     email = driver.find_element(By.CSS_SELECTOR, '#input_16_10')
#     time.sleep(2)
#     email.send_keys("malharmtech@gmail.com")
#     select_ccode = driver.find_element(By.CSS_SELECTOR, "#input_16_26")
#     select_ccode.send_keys("+93")
#     time.sleep(2)
#     mnumber = driver.find_element(By.CSS_SELECTOR, '#input_16_9')
#     time.sleep(2)
#     mnumber.send_keys("5145289574")
#     select_month = driver.find_element(By.CSS_SELECTOR, "#input_2_9_1")
#     select_month.send_keys("5")
#     time.sleep(2)
#     select_day = driver.find_element(By.CSS_SELECTOR, "#input_16_16")
#     select_day.send_keys("04/21/2023")
#     time.sleep(2)
#     modeofcontact = driver.find_element(By.CSS_SELECTOR, "#choice_16_27_1").click()
#     time.sleep(2)
#     next1 = driver.find_element(By.CSS_SELECTOR, "#gform_next_button_16_20").click()
#     time.sleep(10)
#     itemwithsize = driver.find_element(By.CSS_SELECTOR, "#field_16_17 > div.ginput_container.ginput_container_list.ginput_list > table > tbody > tr > td.gfield_list_cell.gfield_list_17_cell1 > select")
#     itemwithsize.send_keys("Heavy-Duty Medium Adjustable TV and Picture Moving Box with Handles")
#     itemquantity = driver.find_element(By.CSS_SELECTOR, "#field_16_17 > div.ginput_container.ginput_container_list.ginput_list > table > tbody > tr > td.gfield_list_cell.gfield_list_17_cell2 > input[type=text]")
#     itemquantity.send_keys("25")
#     inventory = driver.find_element(By.CSS_SELECTOR, "#input_16_11")
#     inventory.send_keys("This is a Automation Testing By- Malhar Chauhan")
#     How = driver.find_element(By.CSS_SELECTOR, "#input_16_23")
#     How.send_keys("Google Search")
#     time.sleep(10)
#     Submit = driver.find_element(By.CSS_SELECTOR, "#gform_submit_button_16").click()
#     time.sleep(10)
#     yield driver
#     driver.quit()


# def browser():
#     driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
#     yield driver
#     driver.quit()
#     driver.find_element(By.CSS_SELECTOR, ".elementor-element-fca7bc1 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)").click()
#     driver.find_element(By.CSS_SELECTOR, 'div.col-xl-12:nth-child(7) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)').click()
#     time.sleep(10)
#     int(driver.execute_script("return document.body.scrollHeight"))
#     for i in range(1, total_height, 5):
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     time.sleep(2)

# # locate the submenu element and hover over it
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
# )
#
# bahrain = driver.find_element(By.CSS_SELECTOR, '.elementor-element-4a39d4f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)

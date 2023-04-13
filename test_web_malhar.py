import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.quit()

def test_website(browser):
    browser.get('https://iss.clients-view.com/')
    assert browser.title == "Moving Company Near Me | Moving Services Near Me | Movers Near Me | ISS Relocations"

def test_website1(browser):
    browser.get('https://iss.clients-view.com/moving-to-bahrain/')
    assert browser.title == "Bahrain Movers | Movers And Packers In Bahrain | Movers In Bahrain"

def test_aboutus(browser):
    browser.get('https://iss.clients-view.com/about/')
    assert browser.title == "About ISS Relocations"

def test_india(browser):
    browser.get('https://iss.clients-view.com/moving-to-india/')
    assert browser.title == "Movers And Packers In India | WareHousing In India | Emigrate To India"

def test_storage_services(browser):
    browser.get('https://iss.clients-view.com/storage-services/')
    assert browser.title == "ISS Relocations Storage Services"

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
    driver.maximize_window()
    driver.get("https://iss.clients-view.com/request-a-quote/")
    fname = driver.find_element(By.ID, 'input_2_5')
    time.sleep(2)
    fname.send_keys("malhar")
    email = driver.find_element(By.ID, 'input_2_6')
    time.sleep(2)
    email.send_keys("malharmtech@gmail.com")
    select_ccode = driver.find_element(By.ID, "input_2_19")
    select_ccode.send_keys("Afghanistan +93")
    time.sleep(2)
    mnumber = driver.find_element(By.ID, 'input_2_8')
    time.sleep(2)
    mnumber.send_keys("5145289574")
    select_month = driver.find_element(By.ID, "input_2_9_1")
    select_month.send_keys("5")
    time.sleep(2)
    select_day = driver.find_element(By.ID, "input_2_9_2")
    select_day.send_keys("20")
    time.sleep(2)
    select_year = driver.find_element(By.ID, "input_2_9_3")
    select_year.send_keys("2023")
    time.sleep(2)
    next1 = driver.find_element(By.CSS_SELECTOR, "#gform_next_button_2_15").click()
    time.sleep(10)
    originaddress = driver.find_element(By.ID, "input_2_1_1")
    originaddress.send_keys("sdfdz")
    originstreetaddress = driver.find_element(By.ID, "input_2_1_3")
    originstreetaddress.send_keys("abauihb")
    originstateaddress = driver.find_element(By.ID, "input_2_1_4")
    originstateaddress.send_keys("sagbsduvb")
    originzipaddress = driver.find_element(By.ID, "input_2_1_5")
    originzipaddress.send_keys("382345")
    origincountry = driver.find_element(By.ID, "input_2_1_6")
    origincountry.send_keys("India")
    destinationaddress = driver.find_element(By.ID, "input_2_4_1")
    destinationaddress.send_keys("euvuavhfebv")
    destinationstreetaddress = driver.find_element(By.ID, "input_2_4_3")
    destinationstreetaddress.send_keys("lkjlhjjbnv")
    destinationstateaddress = driver.find_element(By.ID, "input_2_4_4")
    destinationstateaddress.send_keys("ojhbvgg")
    destinationzipaddress = driver.find_element(By.ID, "input_2_4_5")
    destinationzipaddress.send_keys("382344")
    destinationcountry = driver.find_element(By.ID, "input_2_4_6")
    destinationcountry.send_keys("Algeria")
    next2 = driver.find_element(By.CSS_SELECTOR, "#gform_next_button_2_2").click()
    time.sleep(10)
    itemwithsize = driver.find_element(By.CSS_SELECTOR, "div.gfield_list_group_item:nth-child(1) > input:nth-child(1)")
    itemwithsize.send_keys("chair")
    itemquantity = driver.find_element(By.CSS_SELECTOR, "div.gfield_list_group_item:nth-child(2) > input:nth-child(1)")
    itemquantity.send_keys("lkjlhjjbnv")
    inventory = driver.find_element(By.ID, "input_2_10")
    inventory.send_keys("This is a Automation Testing By Selenium- Malhar Chauhan")
    submit = driver.find_element(By.CSS_SELECTOR, "#gform_submit_button_2").click()
    time.sleep(10)
    yield driver
    driver.quit()

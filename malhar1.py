from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver  import ActionChains
import pdb
import time


# Open a new instance of the Chrome browser and navigate to the website's login page
driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
driver.maximize_window()
driver.get('https://iss.clients-view.com/')
time.sleep(5)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
upside = driver.find_element(By.CSS_SELECTOR, '#scrollUp')

aboutus = driver.find_element(By.CSS_SELECTOR, '#menu-item-572 > a:nth-child(1)').click()
time.sleep(2)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

filebrochure = driver.find_elements_by_tag_name('a').click()



# blog = driver.find_element(By.CSS_SELECTOR, '#menu-item-3991 > a:nth-child(1)').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
# contact = driver.find_element(By.CSS_SELECTOR, '#menu-item-1270 > a:nth-child(1)').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
# requestquote = driver.find_element(By.CSS_SELECTOR, '.elementor-element-c0bc5e7 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
# quickinquiry = driver.find_element(By.CSS_SELECTOR, '.elementor-element-3d1dd0a > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
# time.sleep(2)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
# quickpay = driver.find_element(By.CSS_SELECTOR, '.elementor-element-a53b4ea > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > span:nth-child(1)').click()
# time.sleep(2)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
# bahrain = driver.find_element(By.CSS_SELECTOR, '.elementor-element-9d35bbc > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# India = driver.find_element(By.CSS_SELECTOR, '.elementor-element-9d35bbc > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)

# Kuwait = driver.find_element(By.CSS_SELECTOR, '.elementor-element-61f5c61 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)



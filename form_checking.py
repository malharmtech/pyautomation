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
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
upside = driver.driver.find_element(By.CSS_SELECTOR, '#scrollUp')

requestquote = driver.driver.find_element(By.CSS_SELECTOR, '.elementor-element-c0bc5e7 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
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
mnumber.send_keys("1234578599")
select_month = driver.find_element(By.ID, "input_2_9_1")
select_month.send_keys("5")
time.sleep(2)
select_day = driver.find_element(By.ID, "input_2_9_2")
select_day.send_keys("20")
time.sleep(2)
select_year = driver.find_element(By.ID, "input_2_9_3")
select_year.send_keys("2023")
time.sleep(2)
next1 = driver.driver.find_element(By.CSS_SELECTOR, "#gform_next_button_2_15").click()
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
next2 = driver.driver.find_element(By.CSS_SELECTOR, "#gform_next_button_2_2").click()
time.sleep(10)


itemwithsize = driver.find_element(By.CSS_SELECTOR, "div.gfield_list_group_item:nth-child(1) > input:nth-child(1)")
itemwithsize.send_keys("chair")
itemquantity = driver.find_element(By.CSS_SELECTOR, "div.gfield_list_group_item:nth-child(2) > input:nth-child(1)")
itemquantity.send_keys("lkjlhjjbnv")
inventory = driver.find_element(By.ID, "input_2_10")
inventory.send_keys("This is a Automation Testing By Selenium- Malhar Chauhan")
submit = driver.find_element(By.CSS_SELECTOR, "#gform_submit_button_2").click()
time.sleep(10)



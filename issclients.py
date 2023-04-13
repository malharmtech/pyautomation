from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


urlB = "https://twitter.com/IssRelocations"malhar
# set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://iss.clients-view.com/')


requestquote = driver.find_element(By.CSS_SELECTOR, '.elementor-element-c0bc5e7 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
fname = driver.find_element(By.ID,'input_2_5')
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

homereturn = driver.find_element(By.CSS_SELECTOR, ".elementor-element-fca7bc1 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)").click()


storage = driver.find_element(By.CSS_SELECTOR, 'div.col-xl-12:nth-child(7) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

# locate the submenu element and hover over it
submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
)

bahrain = driver.find_element(By.CSS_SELECTOR, '.elementor-element-4a39d4f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
)

UK = driver.find_element(By.CSS_SELECTOR, '.elementor-element-f77b7be > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
)

Oman = driver.find_element(By.CSS_SELECTOR, '.elementor-element-4a39d4f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1) > span:nth-child(2)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
)

Netherland = driver.find_element(By.CSS_SELECTOR, '.elementor-element-f77b7be > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1) > span:nth-child(2)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
)

NewZealand = driver.find_element(By.CSS_SELECTOR, '.elementor-element-92ef3ef > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
)

brazil = driver.find_element(By.CSS_SELECTOR, '.elementor-element-2737c90 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4063 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-47ccfa8"))
)

MobilityService = driver.find_element(By.CSS_SELECTOR, '.elementor-element-6c71e2f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1) > span:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4063 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-47ccfa8"))
)

petrelocation = driver.find_element(By.CSS_SELECTOR, '.elementor-element-6c71e2f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1) > span:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)


submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-582 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-c61e42f"))
)

gallery = driver.find_element(By.CSS_SELECTOR, '.elementor-element-1ff7081 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > a:nth-child(1) > span:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)


submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-6063 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-fd1b93b"))
)

individuallogin = driver.find_element(By.CSS_SELECTOR, '.elementor-element-4995956 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

quickinquiry = driver.find_element(By.CSS_SELECTOR, '.elementor-element-3d1dd0a > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
time.sleep(2)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

quickpay = driver.find_element(By.CSS_SELECTOR, '.elementor-element-a53b4ea > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > span:nth-child(1)').click()
time.sleep(2)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

blog = driver.find_element(By.CSS_SELECTOR, '#menu-item-3991 > a:nth-child(1)').click()
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

blog1 = driver.find_element(By.CSS_SELECTOR, 'article.postbox:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4) > img:nth-child(1)').click()
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

blog = driver.find_element(By.CSS_SELECTOR, '#menu-item-3991 > a:nth-child(1)').click()
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

contact = driver.find_element(By.CSS_SELECTOR, '#menu-item-1270 > a:nth-child(1)').click()
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

s_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
s_driver.maximize_window()
s_driver.get(urlB)
s_driver.quit()


p_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
p_driver.maximize_window()
p_driver.get("https://in.pinterest.com/issrelocations/")
p_driver.quit()

i_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
i_driver.maximize_window()
i_driver.get("https://www.instagram.com/issrelocations/")
i_driver.quit()

y_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
y_driver.maximize_window()
y_driver.get("https://www.youtube.com/channel/UC3C-PYILNN1Aad28CnpFJ1Q/videos?view_as=subscriber")
y_driver.quit()

driver.quit()





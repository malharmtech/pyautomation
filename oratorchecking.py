from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
urlB = "https://twitter.com/IssRelocations"
# set up the driver
driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
driver.maximize_window()
driver.get('https://oratoracademy.com/')


# locate the submenu element and hover over it
submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-18730 > a:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-18730 > a"))
)

oneonone = driver.find_element(By.CSS_SELECTOR, '#menu-item-20088 > a:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

# locate the submenu element and hover over it
submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-18730 > a:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-18730 > a"))
)

UK = driver.find_element(By.CSS_SELECTOR, '#menu-item-20090 > a:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

# locate the submenu element and hover over it
submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-18730 > a:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#menu-item-18730 > a"))
)

pro = driver.find_element(By.CSS_SELECTOR, '#menu-item-18442 > a:nth-child(1)').click()
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

s_driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
s_driver.maximize_window()
s_driver.get(urlB)
s_driver.quit()


p_driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
p_driver.maximize_window()
p_driver.get("https://in.pinterest.com/issrelocations/")
p_driver.quit()

i_driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
i_driver.maximize_window()
i_driver.get("https://www.instagram.com/issrelocations/")
i_driver.quit()





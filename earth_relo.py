import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.earthrelocation.com/")

time.sleep(2)

# requestquote = driver.find_element(By.CSS_SELECTOR,'body > div.jupiterx-site > header > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-2e50255.elementor-section-stretched.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default.jet-parallax-section > div.elementor-container.elementor-column-gap-no > div > div.elementor-column.elementor-col-33.elementor-top-column.elementor-element.elementor-element-c682bb2.elementor-hidden-tablet.elementor-hidden-phone > div > div > div > div > div > a').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#
# driver.get("https://www.earthrelocation.com/free-online-moving-quote/")
# originaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_1_1")
# originaddress.send_keys("sdfdz")
# originstreetaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_1_3")
# originstreetaddress.send_keys("abauihb")
# originstateaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_1_4")
# originstateaddress.send_keys("sagbsduvb")
# originzipaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_1_5")
# originzipaddress.send_keys("382345")
# origincountry = driver.find_element(By.CSS_SELECTOR,"#input_16_1_6")
# origincountry.send_keys("India")
# destinationaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_2_1")
# destinationaddress.send_keys("euvuavhfebv")
# destinationstreetaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_2_3")
# destinationstreetaddress.send_keys("lkjlhjjbnv")
# destinationstateaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_2_4")
# destinationstateaddress.send_keys("ojhbvgg")
# destinationzipaddress = driver.find_element(By.CSS_SELECTOR,"#input_16_2_5")
# destinationzipaddress.send_keys("382344")
# destinationcountry = driver.find_element(By.CSS_SELECTOR,"#input_16_2_6")
# destinationcountry.send_keys("Algeria")
# fname = driver.find_element(By.CSS_SELECTOR,'#input_16_8')
# time.sleep(2)
# fname.send_keys("malhar")
# lname = driver.find_element(By.CSS_SELECTOR,'#input_16_25')
# time.sleep(2)
# lname.send_keys("chauhan")
# email = driver.find_element(By.CSS_SELECTOR,'#input_16_10')
# time.sleep(2)
# email.send_keys("malharmtech@gmail.com")
# select_ccode = driver.find_element(By.CSS_SELECTOR,"#input_16_26")
# select_ccode.send_keys("+93")
# time.sleep(2)
# mnumber = driver.find_element(By.CSS_SELECTOR,'#input_16_9')
# time.sleep(2)
# mnumber.send_keys("5145289574")
# select_day = driver.find_element(By.CSS_SELECTOR,"#input_16_16")
# select_day.send_keys("04/21/2023")
# time.sleep(2)
# modeofcontact = driver.find_element(By.CSS_SELECTOR,"#choice_16_27_1").click()
# time.sleep(2)
# next1 = driver.find_element(By.CSS_SELECTOR,"#gform_next_button_16_20").click()
# time.sleep(10)
# itemwithsize = driver.find_element(By.CSS_SELECTOR,"#field_16_17 > div.ginput_container.ginput_container_list.ginput_list > table > tbody > tr > td.gfield_list_cell.gfield_list_17_cell1 > select > option:nth-child(1)")
# itemquantity = driver.find_element(By.CSS_SELECTOR,"#field_16_17 > div.ginput_container.ginput_container_list.ginput_list > table > tbody > tr > td.gfield_list_cell.gfield_list_17_cell2 > input[type=text]")
# itemquantity.send_keys("25")
# inventory = driver.find_element(By.CSS_SELECTOR,"#input_16_11")
# inventory.send_keys("This is a Automation Testing By- Malhar Chauhan")
# How = driver.find_element(By.CSS_SELECTOR,"#input_16_23")
# How.send_keys("Google Search")
# time.sleep(10)
# Submit = driver.find_element(By.CSS_SELECTOR,"#gform_submit_button_16").click()
# time.sleep(10)


# locate the submenu element and hover over it
submenu = driver.find_element(By.CSS_SELECTOR,"#menu-item-93953 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-16371636"))
)

India = driver.find_element(By.CSS_SELECTOR,'.elementor-element-5b10041e > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

# locate the submenu element and hover over it
submenu = driver.find_element(By.CSS_SELECTOR,"#menu-item-93954 > a:nth-child(1) > i:nth-child(1)")
hover = ActionChains(driver).move_to_element(submenu)
hover.perform()

submenu_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-6da5c71"))
)

Toronto = driver.find_element(By.CSS_SELECTOR,'.elementor-element-ad3521a > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)').click()
time.sleep(10)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)


# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
# )
#
# UK = driver.find_element(By.CSS_SELECTOR, '.elementor-element-f77b7be > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
# )
#
# Oman = driver.find_element(By.CSS_SELECTOR, '.elementor-element-4a39d4f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
# )
#
# Netherland = driver.find_element(By.CSS_SELECTOR, '.elementor-element-f77b7be > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
# )
#
# NewZealand = driver.find_element(By.CSS_SELECTOR, '.elementor-element-92ef3ef > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4640 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-f5e7e08"))
# )
#
# brazil = driver.find_element(By.CSS_SELECTOR, '.elementor-element-2737c90 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > span:nth-child(2)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4063 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-47ccfa8"))
# )
#
# MobilityService = driver.find_element(By.CSS_SELECTOR, '.elementor-element-6c71e2f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1) > span:nth-child(1)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-4063 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-47ccfa8"))
# )
#
# petrelocation = driver.find_element(By.CSS_SELECTOR, '.elementor-element-6c71e2f > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1) > span:nth-child(1)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-582 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-c61e42f"))
# )
#
# gallery = driver.find_element(By.CSS_SELECTOR, '.elementor-element-1ff7081 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > a:nth-child(1) > span:nth-child(1)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
#
# submenu = driver.find_element(By.CSS_SELECTOR, "#menu-item-6063 > a:nth-child(1) > i:nth-child(1)")
# hover = ActionChains(driver).move_to_element(submenu)
# hover.perform()
#
# submenu_items = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".elementor-element-fd1b93b"))
# )
#
# individuallogin = driver.find_element(By.CSS_SELECTOR, '.elementor-element-4995956 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()
# time.sleep(10)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# quickinquiry = driver.find_element(By.CSS_SELECTOR, '.elementor-element-3d1dd0a > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
# time.sleep(2)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# quickpay = driver.find_element(By.CSS_SELECTOR, '.elementor-element-a53b4ea > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > span:nth-child(1)').click()
# time.sleep(2)
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# blog = driver.find_element(By.CSS_SELECTOR, '#menu-item-3991 > a:nth-child(1)').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# blog1 = driver.find_element(By.CSS_SELECTOR, 'article.postbox:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4) > img:nth-child(1)').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# blog = driver.find_element(By.CSS_SELECTOR, '#menu-item-3991 > a:nth-child(1)').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# contact = driver.find_element(By.CSS_SELECTOR, '#menu-item-1270 > a:nth-child(1)').click()
# total_height = int(driver.execute_script("return document.body.scrollHeight"))
# for i in range(1, total_height, 5):
#     driver.execute_script("window.scrollTo(0, {});".format(i))
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(2)
#
# s_driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
# s_driver.maximize_window()
# s_driver.get(urlB)
# s_driver.quit()
#
#
# p_driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
# p_driver.maximize_window()
# p_driver.get("https://in.pinterest.com/issrelocations/")
# p_driver.quit()
#
# i_driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
# i_driver.maximize_window()
# i_driver.get("https://www.instagram.com/issrelocations/")
# i_driver.quit()

driver.quit()





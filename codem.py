from selenium import webdriver
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

# specify the path to the chromedriver executable
chromedriver_path = 'path/to/chromedriver'

# create a new Chrome browser instance
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()

# navigate to Google
browser.get('https://www.google.com')

# locate the search box and enter a query
search_box = browser.find_element(By.NAME, 'q')
search_box.send_keys('python selenium')

# submit the query and wait for the results page to load
search_box.submit()
browser.implicitly_wait(10)

# locate all the search result links and print their href attribute
search_results = (browser.find_elements(By.TAG_NAME, 'h3')).text
for result in search_results:
    print(result.get_attribute('href'))

# close the browser
browser.quit()

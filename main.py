from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# initialize
webdriver_path = "C:\\Users\\venislav.zdravkov\chromedriver_win32\chromedriver"
service = Service(executable_path=webdriver_path)

# open chrome driver
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

# go to url

driver.get("http://mydemostore.local/")
time.sleep(3)

# click on my account
my_account_tab = driver.find_element(By.LINK_TEXT, "My account")
my_account_tab.click()
time.sleep(3)

driver.quit()

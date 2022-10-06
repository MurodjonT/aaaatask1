from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)

driver.get("https://store.steampowered.com/")




# driver.find_element(By.ID, "search-input").send_keys("Samsung Galaxy A33 5G 6/128GB")
###############################################################################################Login PART
########CSS_SELECTOR, "input.valueofclass"
driver.find_element(By.LINK_TEXT, "login").click()
input_field = driver.find_element(By.CSS_SELECTOR, "input.newlogindialog_TextInput_2eKVn")
input_field.send_keys("asd")


##################################################################################PASSWORD PART
input_field1 = driver.find_element(By.XPATH, "//input[@type='password']")
input_field1.send_keys("asjdh2312")  # insert your password here
input_field1.submit()
time.sleep(1)




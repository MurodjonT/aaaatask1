from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Patterns.singleton import Singleton
from Config.config import TestData

class BasePage(metaclass=Singleton):
    
    """Parent class"""

    
    def __init__(self, driver):
        self.driver = driver

    

    def do_click(self, by_locator):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.element_to_be_clickable(by_locator)).click()
    
    
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    

    def get_list(self, by_locator):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).find_elements()
    

    def get_element_text(self, by_locator):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).text
    

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    def excute_scroll(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

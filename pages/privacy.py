from Config.config import TestData
from Config import urldata
from .home_page import BasePage
from selenium.webdriver.common.by import By

class PolicyPage(BasePage):
    
    """Policy class"""

    TEXT = (By.XPATH, '//*[@id="newsColumn"]/i[3]')
    POLICY_BUTTON = (By.XPATH, '//*[@id="footer_text"]/div[2]/a[1]')
    LANGUAGES_ELEMENETS = (By.XPATH, '//*[@id="languages"]/a')
    

    def do_click_button(self):
        return self.do_click(self.POLICY_BUTTON)

    def get_policy_page_title(self):
        return self.get_title(title)

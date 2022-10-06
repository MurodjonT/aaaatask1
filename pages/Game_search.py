from Config.config import TestData
from .home_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    """Search class"""

    SEARCH_INPUT = (By.XPATH, '//*[@id="store_nav_search_term"]')
    SEARCH_INPUT_LIST = (By.XPATH, '//*[@id="search_suggestion_contents"]/a')

    
    def do_search(self, keyword):
        return self.do_send_keys(self.SEARCH_INPUT, keyword)
    
    def get_search_list(self):
        return self.get_list(self.SEARCH_INPUT_LIST)

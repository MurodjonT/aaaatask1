from Config.config import TestData
import pytest
from Pages.search import SearchPage
from Config.config import read_file
from Config import urldata


@pytest.mark.usefixtures("init_driver")
class TestSearch():
  
    def test_search_page(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.driver.get(urldata.BASE_URL)
        self.searchPage.do_search(TestData.SEARCH)
        elements = self.searchPage.get_search_list()
        assert elements == read_file("Config/search.txt")

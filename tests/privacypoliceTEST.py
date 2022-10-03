from Config.config import TestData
import pytest
from Pages.policy import PolicyPage
from Config import urldata

@pytest.mark.usefixtures("init_driver")
class TestPolicy():
    def test_policy_page(self):
        self.policyPage = PolicyPage(self.driver)
        self.policyPage.driver.get(urldata.BASE_URL)
        self.policyPage.excute_scroll()
        self.policyPage.do_click_button()
        text = self.policyPage.get_element_text(TestData.POLICY_PAGE_TEXT)
        assert text == TestData.POLICY_PAGE_TEXT



import pytest
from selenium import webdriver
from Config.config import TestData
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    request.cls.driver = web_driver 
    yield
    web_driver.quit()

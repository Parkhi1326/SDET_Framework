import pytest
from selenium import webdriver

from POM_Class.Search import SearchBox
class TestSearch:
    def test_search(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()
        ts=SearchBox(driver)
        ts.setText("Dresses")
        ts.clickBtn()
        act_title=driver.title
        assert act_title=="Search - My Shop"

        # C:\Users\parve\PycharmProjects\SDET_10_01\Frameworks\TestClass\test_search.py
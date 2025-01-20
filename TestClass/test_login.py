import pytest
from selenium import webdriver

from POM_Class.Login import LoginPage

class TestLogin:
    def test_login(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(5)
        driver.maximize_window()
        lp=LoginPage(driver)
        lp.setUserName("parkhigera@gmail.com")
        lp.setUserPassword("Parkhi123")
        lp.clickBtn()
        act_title=driver.title
        assert act_title=="Login - My Shop"

# C:\Users\parve\PycharmProjects\SDET_10_01\Frameworks\TestClass\test_login.py

#
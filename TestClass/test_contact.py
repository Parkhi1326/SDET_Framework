import pytest
from selenium import webdriver

from POM_Class.ContactUs import ContactUS
class TestContact:
    def test_contact(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=contact")
        driver.implicitly_wait(5)
        driver.maximize_window()
        cp=ContactUS(driver)

        cp.setEmail('parkhigera@gmail.com')
        cp.setRef("101")
        cp.clickBtn()
        act_title=driver.title
        assert act_title=="Contact us - My Shop"
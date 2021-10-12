import time


import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utility.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_fromSubmission(self,getData):
        log = self.getLogger()

        #driver.find_element_by_css_selector("input[name='name']").send_keys("Shankar")
        homePage = HomePage(self.driver)
        log.info("First name is :" +getData["firstname"])
        homePage.getUserName().send_keys(getData["firstname"])
        time.sleep(1)


        #driver.find_element_by_name("email").send_keys("rahulsetti@gmail.com")
        log.info("Last name is:" + getData["lastname"])
        homePage.getEmail().send_keys(getData["lastname"])
        time.sleep(1)

        #driver.find_element_by_id("exampleCheck1").click()
        homePage.setCheckBox().click()
        time.sleep(1)


        # select class provides  methods to handle the options in drop down
        #dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        #dropdown.select_by_visible_text("Female")
        #dropdown = Select(homePage.clickDropDown())
        #dropdown.select_by_visible_text("Female")
        #dropdown.select_by_index(0)
        self.selectOptionByText(homePage.clickDropDown(), getData["gender"])
        time.sleep(1)


        #driver.find_element_by_xpath("//input[@type='submit']").click()
        homePage.clickSubmitBtn().click()
        time.sleep(1)

        # print(driver.find_element_by_class_name("alert-success").text)

        #message = driver.find_element_by_css_selector("[class*=alert-success]").text
        # //*[contains(@class,'alert-success')]
        message = homePage.getSuccessMsg().text
        assert "Success" in message
        time.sleep(1)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


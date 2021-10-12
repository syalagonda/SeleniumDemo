import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utility.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        # Home Page ############################################
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the titles ")
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()

        # CheckoutPage ##########################################
        #checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getCardTitles()
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        # //div[@class='card h-100']/div/h4/a

        for product in products:
            prodName = product.find_element_by_xpath("div/h4/a").text
            log.info(prodName)
            if prodName == "Blackberry":
                product.find_element_by_xpath("div/button").click()
                #checkOutPage.getCardFooter().click()
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        #checkOutPage.getCheckOutItems().click()
        confirmPage = checkOutPage.getCheckOutItems()

        # ConfirPage ###########################################
        #self.driver.find_element_by_id("country").send_keys("ind")
        #confirmPage = ConfirmPage(self.driver)
        log.info("Entering country name to Ind")
        confirmPage.setCountryName().send_keys("ind")

        ########################################################################################
        # explicit wait, method developed in Base class
        #wait = WebDriverWait(self.driver, 6)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        ###########################################################################################
        self.verifyLinkPresence("India")

        #self.driver.find_element_by_link_text("India").click()
        confirmPage.selectCountryName().click()

        #self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirmPage.clickCheckBox().click()


        #self.driver.find_element_by_css_selector("input[type='submit']").click()
        confirmPage.clickSubmit().click()


        #successText = self.driver.find_element_by_class_name("alert-success").text
        successText = confirmPage.getConfirmText().text
        log.info(successText)
        assert "Success! Thank you!" in successText



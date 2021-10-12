from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH,"//div[@class='card h-100']")
    cardFooter = (By.XPATH,"div/button")
    checkOut = (By.XPATH,"//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    #def getCardFooter(self):
        #return self.driver.find_element(*CheckOutPage.cardFooter)

    def getCheckOutItems(self):
        #return self.driver.find_element(*CheckOutPage.checkOut)
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage



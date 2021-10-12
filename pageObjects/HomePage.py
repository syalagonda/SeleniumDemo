from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    dropDown = (By.ID, "exampleFormControlSelect1")

    submitBtn = (By.XPATH, "//input[@type='submit']")
    succesMesg = (By.CSS_SELECTOR, "[class*=alert-success]")

    def shopItems(self):
        #return self.driver.find_element(*HomePage.shop)
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getUserName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def setCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def clickDropDown(self):
        return self.driver.find_element(*HomePage.dropDown)

    def clickSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.succesMesg)



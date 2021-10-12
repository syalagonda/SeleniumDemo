from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    setName = (By.ID, "country")
    selectName = (By.LINK_TEXT, "India")
    checkBox= (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitForm = (By.CSS_SELECTOR, "input[type='submit']")
    confirmText = (By.CLASS_NAME, "alert-success")



    def setCountryName(self):
        return self.driver.find_element(*ConfirmPage.setName)

    def selectCountryName(self):
        return self.driver.find_element(*ConfirmPage.selectName)

    def clickCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def clickSubmit(self):
        return self.driver.find_element(*ConfirmPage.submitForm)

    def getConfirmText(self):
       return self.driver.find_element(*ConfirmPage.confirmText)

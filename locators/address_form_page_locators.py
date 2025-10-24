from selenium.webdriver.common.by import By


class AddressFormPageLocators:
    ADDRESS_FROM_INPUT = By.XPATH, "//input[@id='from']"
    ADDRESS_TO_INPUT = By.XPATH, "//input[@id='to']"
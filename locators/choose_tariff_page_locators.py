from selenium.webdriver.common.by import By


class ChooseTariffPageLocators:
    TARIFF_BUTTON = By.XPATH, "//div[contains(@class,'tcard') and contains(., {})]"
    TARIFF_INFORMATION_BUTTON = By.XPATH, "//button[@data-for='tariff-card-{}']"
    TARIFF_INFORMATION_POPUP = By.XPATH, "(//div[@id='tariff-card-{}'])"
    ACTIVE_TARIFF_BUTTON = By.XPATH, "//div[@class='tcard active']"
    TARIFF_INFORMATION_TITLE = By.XPATH, "(//div[@class='i-title'])[{}]"
    TARIFF_INFORMATION_DESCRIPTION = By.XPATH, "(//div[@class='i-dPrefix'])[{}]"
    TARIFF_PRICE = By.XPATH, "(//div[@class='tcard-price'])[{}]"
    PHONE_INPUT = By.XPATH, "//div[@class='np-button']"
    PAYMENT_OPTION_INPUT = By.XPATH, "//div[@class='pp-button filled']"
    COMMENT_INPUT = By.XPATH, "//input[@id='comment']"
    REQUIREMENTS_DROPDOWN = By.XPATH, "//div[@class='reqs']"
    REQUIREMENTS_DROPDOWN_BUTTON = By.XPATH, "//div[@class='reqs-arrow']"
    LAPTOP_SWITCH = By.XPATH, "//div[@class='switch']"
    ORDER_TAXI_SUBMIT_BUTTON = By.XPATH, "//button[@class='smart-button']"


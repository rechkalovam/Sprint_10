from selenium.webdriver.common.by import By


class WaitingOrderPageLocators:
    WAITING_ORDER_WINDOW = By.XPATH, "//div[@class='order-body']"
    WAITING_ORDER_TITLE = By.XPATH, "//div[@class='order-header-title']"
    ORDER_WAIT_TIME = By.XPATH, "//div[@class='order-header-time']"
    WAITING_ORDER_CANCEL_BUTTON = By.XPATH, "//div[text()='Отменить']/preceding-sibling::button"
    WAITING_ORDER_DETAILS_BUTTON = By.XPATH, "//div[text()='Детали']/preceding-sibling::button"
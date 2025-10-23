from selenium.webdriver.common.by import By


class OrderInfoPageLocators:
    ORDER_WINDOW = By.XPATH, "//div[@class='order-body']"
    ORDER_TITLE = By.XPATH, "//div[@class='order-header-title']"
    ORDER_CAR_NUMBER = By.XPATH, "//div[@class='number']"
    ORDER_CAR_IMAGE = By.XPATH, "//div[@class='order-number']/img"
    ORDER_DRIVER_PHOTO = By.XPATH, "//div[@class='order-button']/img"
    ORDER_DRIVER_RATING = By.XPATH, "//div[@class='order-btn-rating']"
    ORDER_DRIVER_NAME = By.XPATH, "(//div[@class='order-btn-group'])[1]/div[2]"
    ORDER_CANCEL_BUTTON = By.XPATH, "//div[text()='Отменить']/preceding-sibling::button"
    ORDER_DETAILS_BUTTON = By.XPATH, "//div[text()='Детали']/preceding-sibling::button"
    ORDER_DETAILS_PRICE = By.XPATH, "//div[contains(text(),'Стоимость')]"
from selenium.webdriver.common.by import By


class ChooseRoutePageLocators:
    CHOOSE_ROUTE_BLOCK = By.XPATH, "//div[@class='type-picker shown']"
    ROUTE_PRICE_TEXT = By.XPATH, "//div[@class='text']"
    ROUTE_DURATION_TEXT = By.XPATH, "//div[@class='duration']"
    OPTIMAL_ROUTE_TAB = By.XPATH, "//div[text()='Оптимальный']"
    FAST_ROUTE_TAB = By.XPATH, "//div[text()='Быстрый']"
    MINE_ROUTE_TAB = By.XPATH, "//div[text()='Свой']"
    ACTIVE_ROUTE_TAB = By.XPATH, "//div[@class='mode active']"
    SELECTED_TRANSPORT_TAB = By.XPATH, "//div[contains(@class,'type') and contains(@class,'active')]"
    AVAILABLE_TRANSPORT_TABS = By.XPATH, "//div[@class='type' or @class='type drive']"
    DISABLE_TRANSPORT_TABS = By.XPATH, "//div[contains(@class,'type') and contains(@class,'disabled')]"
    DRIVE_TRANSPORT_TAB = By.XPATH, "//div[contains(@class,'type') and contains(@class,'drive')]"
    ORDER_TAXI_BUTTON = By.XPATH, "//button[text()='Вызвать такси']"
    RESERVE_CAR_BUTTON = By.XPATH, "//button[text()='Забронировать']"
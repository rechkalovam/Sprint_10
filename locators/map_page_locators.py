from selenium.webdriver.common.by import By
import data


class MapPageLocators:
    MAP_LOCATION_A = By.XPATH,  f'//ymaps[contains(normalize-space(text()), "{data.LOCATION_A}")]'
    MAP_LOCATION_B = By.XPATH, f'//ymaps[contains(normalize-space(text()), "{data.LOCATION_B}")]'
import allure
from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.map_page_locators import MapPageLocators


class MapPage(BasePage):

    @allure.step('Проверка видимости на карте точки А')
    def check_visibility_of_point_a(self):
        try:
            self.find_element_with_wait(MapPageLocators.MAP_LOCATION_A)
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False


    @allure.step('Проверка видимости на карте точки В')
    def check_visibility_of_point_b(self):
        try:
            self.find_element_with_wait(MapPageLocators.MAP_LOCATION_B)
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False
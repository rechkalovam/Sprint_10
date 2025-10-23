import allure
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.choose_route_page_locators import ChooseRoutePageLocators


class ChooseRoutePage(BasePage):

    @allure.step('Проверка отображения блока выбора маршрута')
    def check_visibility_of_choose_route_block(self):
        return self.find_element_with_wait(ChooseRoutePageLocators.CHOOSE_ROUTE_BLOCK)

    @allure.step('Получение текста стоимости поездки')
    def get_address_price_text_block(self):
        return self.get_text_from_element(ChooseRoutePageLocators.ROUTE_PRICE_TEXT)

    @allure.step('Получение текста длительности поездки')
    def get_address_duration_text_block(self):
        return self.get_text_from_element(ChooseRoutePageLocators.ROUTE_DURATION_TEXT)

    @allure.step('Клик на таб маршрута "Оптимальный"')
    def click_to_optimal_route_tab(self):
        self.click_to_element(ChooseRoutePageLocators.OPTIMAL_ROUTE_TAB)

    @allure.step('Клик на таб маршрута "Быстрый"')
    def click_to_fast_route_tab(self):
        self.click_to_element(ChooseRoutePageLocators.FAST_ROUTE_TAB)

    @allure.step('Клик на таб маршрута "Свой"')
    def click_to_mine_route_tab(self):
        self.click_to_element(ChooseRoutePageLocators.MINE_ROUTE_TAB)

    @allure.step('Получение текста активного таба маршрута')
    def check_active_route_tab_text(self):
        return self.get_text_from_element(ChooseRoutePageLocators.ACTIVE_ROUTE_TAB)

    @allure.step('Проверка доступности табов выбора транспорта')
    def check_transport_tabs_are_available(self):
        try:
            self.wait_until_element_is_invisible(ChooseRoutePageLocators.DISABLE_TRANSPORT_TABS)
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False


    @allure.step('Проверка отображения кнопки "Вызвать такси"')
    def check_order_taxi_button_is_available(self):
        try:
            self.find_element_with_wait(ChooseRoutePageLocators.ORDER_TAXI_BUTTON)
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False

    @allure.step('Клик на кнопку "Вызвать такси"')
    def click_to_order_taxi_button(self):
        self.click_to_element(ChooseRoutePageLocators.ORDER_TAXI_BUTTON)

    @allure.step('Клик на кнопку "Забронировать"')
    def click_to_drive_transport_tab(self):
        self.click_to_element(ChooseRoutePageLocators.DRIVE_TRANSPORT_TAB)

    @allure.step('Проверка отображения кнопки "Забронировать"')
    def check_reserve_car_button_is_available(self):
        try:
            self.find_element_with_wait(ChooseRoutePageLocators.RESERVE_CAR_BUTTON)
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False


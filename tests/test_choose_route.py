import sys
import allure
from pathlib import Path

from conftest import fill_addresses

sys.path.append(str(Path(__file__).parent.parent))
from pages.address_form_page import AddressFormPage
from pages.choose_route_page import ChooseRoutePage
from urls import URL_MAIN_PAGE
from data import SAME_ADDRESS_PRICE_TEXT, FAST_ROUTE_TAB_TEXT, OPTIMAL_ROUTE_TAB_TEXT, \
    MINE_ROUTE_TAB_TEXT, SAME_ADDRESS_DURATION_TEXT


class TestChooseRoutePage:

    @allure.title("Проверка отображения блока выбора маршрута при вводе двух разных адресов")
    def test_route_selection_block_displayed_for_different_addresses(self, driver):
        address_form = AddressFormPage(driver)
        address_form.go_to_url(URL_MAIN_PAGE)
        address_form.add_addresses_to_address_form()
        choose_route_page = ChooseRoutePage(driver)
        assert choose_route_page.check_visibility_of_choose_route_block(), 'Блок выбора маршрута не отображается'

    @allure.title("Проверка отображения текста в блоке выбора маршрута при вводе двух одинаковых адресов")
    def test_route_block_displayed_for_same_addresses_with_text(self, driver):
        address_form = AddressFormPage(driver)
        address_form.go_to_url(URL_MAIN_PAGE)
        address_form.add_same_address_to_address_form()
        choose_route_page = ChooseRoutePage(driver)
        price_text = choose_route_page.get_address_price_text_block()
        duration_text = choose_route_page.get_address_duration_text_block()
        assert (price_text == SAME_ADDRESS_PRICE_TEXT and duration_text == SAME_ADDRESS_DURATION_TEXT), \
            f"Текст стоимости поездки: {price_text}, текст длительности поездки: {duration_text}"

    #в задании написано проверить смену и длительности маршрута, но в данном случае длительность на авто и такси одинаковая
    @allure.title("Проверка изменения стоимости поездки при смене маршрута на 'Оптимальный'")
    def test_click_to_optimal_route_changes_active_tab_and_updates_values(self, fill_addresses):
        old_price_text = fill_addresses.get_address_price_text_block()
        fill_addresses.click_to_optimal_route_tab()
        active_tab_text = fill_addresses.check_active_route_tab_text()
        assert active_tab_text == OPTIMAL_ROUTE_TAB_TEXT and fill_addresses.get_address_price_text_block() != old_price_text, \
            f'Активный таб после клика на "Оптимальный": {active_tab_text}'

    @allure.title("Проверка изменения стоимости поездки при смене маршрута на 'Быстрый'")
    def test_click_to_fast_route_changes_active_tab_and_updates_values(self, fill_addresses):
        fill_addresses.click_to_optimal_route_tab()
        old_price_text = fill_addresses.get_address_price_text_block()
        fill_addresses.click_to_fast_route_tab()
        active_tab_text = fill_addresses.check_active_route_tab_text()
        assert active_tab_text == FAST_ROUTE_TAB_TEXT and fill_addresses.get_address_price_text_block() != old_price_text, \
            f'Активный таб после клика на "Быстрый": {active_tab_text}'

    @allure.title("Проверка доступности табов транспорта при смене маршрута на 'Свой'")
    def test_switch_to_mine_route_activates_transport_types(self, fill_addresses):
        fill_addresses.click_to_mine_route_tab()
        active_tab_text = fill_addresses.check_active_route_tab_text()
        transport_tabs = fill_addresses.check_transport_tabs_are_available()
        assert active_tab_text == MINE_ROUTE_TAB_TEXT and transport_tabs == True, \
            f'Активный таб после клика на "Свой": {active_tab_text}, доступность табов транспорта: {transport_tabs}'

    @allure.title("Проверка доступности кнопки 'Вызвать такси' при выборе маршрута 'Быстрый'")
    def test_taxi_button_available_when_fast_route_selected(self, fill_addresses):
        active_tab_text = fill_addresses.check_active_route_tab_text()
        order_taxi_button = fill_addresses.check_order_taxi_button_is_available()
        assert active_tab_text == FAST_ROUTE_TAB_TEXT and fill_addresses.check_order_taxi_button_is_available(), \
            f'Активный таб после клика на "Быстрый": {active_tab_text}, доступность кнопки: {order_taxi_button}'

    @allure.title("Проверка доступности кнопки 'Забронировать' при выборе транспорта 'Драйв' и маршрута 'Свой'")
    def test_mine_route_drive_enables_reserve_button(self, fill_addresses):
        fill_addresses.click_to_mine_route_tab()
        fill_addresses.click_to_drive_transport_tab()
        reserve_button = fill_addresses.check_reserve_car_button_is_available()
        assert reserve_button == True, f'Доступность кнопки: {reserve_button}'

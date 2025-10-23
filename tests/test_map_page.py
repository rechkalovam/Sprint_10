import sys
import allure
from pathlib import Path
from pages.map_page import MapPage
sys.path.append(str(Path(__file__).parent.parent))
from pages.address_form_page import AddressFormPage
from urls import URL_MAIN_PAGE


class TestMapPage:

    @allure.title('Проверка отображения на карте точек начала и конца маршрута при вводе двух разных адресов')
    def test_route_start_and_end_points_displayed_on_map(self, driver):
        address_form = AddressFormPage(driver)
        address_form.go_to_url(URL_MAIN_PAGE)
        address_form.add_addresses_to_address_form()
        map_page = MapPage(driver)
        point_a = map_page.check_visibility_of_point_a()
        point_b = map_page.check_visibility_of_point_b()
        assert point_a == True and point_b == True, f'Видимость точки A: {point_a}, Видимость точки B: {point_b}'
import sys
import allure
from pathlib import Path
import pytest
sys.path.append(str(Path(__file__).parent.parent))
from data import ORDER_INFO_PAGE_TITLE


class TestOrderInfoPage:

    @allure.title("Проверка отображения окна информации о заказе")
    def test_check_visibility_of_order_info_page(self, finish_order):
        price, finish_order = finish_order
        assert (finish_order.check_visibility_of_order_info_block() and finish_order.get_title_text_of_order_info_page() == ORDER_INFO_PAGE_TITLE
                and finish_order.check_visibility_of_order_info_block_details()), "Окно информации о заказе не отображается"

    @allure.title("Проверка совпадения стоимости поездки в деталях информации о заказе и окне выбора тарифа")
    def test_order_info_details_show_correct_tariff_price(self, finish_order):
        price, finish_order = finish_order
        finish_order.click_to_order_info_details_button()
        order_price = finish_order.get_order_price_to_order_details()
        assert order_price == price, f'Цена при выборе тарифа: {price}, цена в деталях информации о заказе: {order_price}'

    @allure.title("Проверка закрытия окна информации о заказе при нажатии на кнопку 'Отменить'")
    @pytest.mark.xfail(reason="Баг - Кнопка 'Отменить' не закрывает окно деталей поездки")
    def test_cancel_button_closes_order_info_page(self, finish_order):
        price, finish_order = finish_order
        finish_order.click_to_order_info_cancel_button()
        assert finish_order.check_invisibility_of_order_info_block(), "Окно информации о заказе отображается при нажатии на кнопку 'Отменить'"

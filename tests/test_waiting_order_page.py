import sys
import allure
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from data import WAITING_ORDER_PAGE_TITLE


class TestWaitingOrderPage:

    @allure.title("Проверка отображения окна ожидания информации о заказе")
    def test_check_visibility_of_waiting_order_page(self, order_taxi):
        price, waiting_order_page = order_taxi
        waiting_order_block = waiting_order_page.check_visibility_of_waiting_order_block()
        title = waiting_order_page.get_title_text_of_waiting_order_page()
        waiting_order_block_details = waiting_order_page.check_visibility_of_waiting_order_details()
        assert (waiting_order_block == True and title == WAITING_ORDER_PAGE_TITLE
                and waiting_order_block_details == True), \
            f'Отображение окна ожидания: {waiting_order_block}, текст заголовка окна: {title}, отображение деталей окна: {waiting_order_block_details}'

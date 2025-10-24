import allure
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.waiting_order_page_locators import WaitingOrderPageLocators


class WaitingOrderPage(BasePage):

    @allure.step('Проверка отображения окна ожидания информации о заказе')
    def check_visibility_of_waiting_order_block(self):
        try:
            self.find_element_with_wait(WaitingOrderPageLocators.WAITING_ORDER_WINDOW)
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False

    @allure.step('Проверка отображения заголовка окна ожидания информации о заказе')
    def check_visibility_of_waiting_order_title(self):
        return self.find_element_with_wait(WaitingOrderPageLocators.WAITING_ORDER_TITLE)

    @allure.step('Проверка отображения таймера ожидания информации о заказе')
    def check_visibility_of_waiting_order_timer(self):
        return self.find_element_with_wait(WaitingOrderPageLocators.ORDER_WAIT_TIME)

    @allure.step('Проверка отображения кнопки "Детали" в окне ожидания информации о заказе')
    def check_visibility_of_waiting_order_details_button(self):
        return self.find_element_with_wait(WaitingOrderPageLocators.WAITING_ORDER_DETAILS_BUTTON)

    @allure.step('Проверка отображения кнопки "Отменить" в окне ожидания информации о заказе')
    def check_visibility_of_waiting_order_cancel_button(self):
        return self.find_element_with_wait(WaitingOrderPageLocators.WAITING_ORDER_CANCEL_BUTTON)

    @allure.step('Проверка отображения деталей в окне ожидания информации о заказе')
    def check_visibility_of_waiting_order_details(self):
        try:
            self.check_visibility_of_waiting_order_title()
            self.check_visibility_of_waiting_order_timer()
            self.check_visibility_of_waiting_order_details_button()
            self.check_visibility_of_waiting_order_cancel_button()
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False

    @allure.step('Получение текста заголовка окна ожидания информации о заказе')
    def get_title_text_of_waiting_order_page(self):
        return self.get_text_from_element(WaitingOrderPageLocators.WAITING_ORDER_TITLE)

    @allure.step('Ожидание окончания таймера ожидания информации о заказе')
    def wait_until_waiting_order_timer_is_done(self):
        old_title = self.get_title_text_of_waiting_order_page()
        self.wait_text_in_element(WaitingOrderPageLocators.ORDER_WAIT_TIME, "00:00")
        self.wait_change_text_in_element_without_new_text(WaitingOrderPageLocators.WAITING_ORDER_TITLE, old_title)
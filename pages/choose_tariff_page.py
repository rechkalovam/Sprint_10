import allure
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.choose_tariff_page_locators import ChooseTariffPageLocators
from helpers import HelpersMethods


class ChooseTariffPage(BasePage):

    @allure.step('Проверка отображения блока тарифов')
    def check_visibility_of_tariffs(self, name):
        formatted_tariff = self.format_locators(ChooseTariffPageLocators.TARIFF_BUTTON, name)
        return self.find_element_with_wait(formatted_tariff)

    @allure.step('Проверка отображения активного тарифа')
    def check_visibility_of_active_tariff(self):
        return self.find_element_with_wait(ChooseTariffPageLocators.ACTIVE_TARIFF_BUTTON)

    @allure.step('Клик на тариф в блоке тарифов')
    def click_to_tariff_button(self, num):
        formatted_tariff = self.format_locators(ChooseTariffPageLocators.TARIFF_INFORMATION_BUTTON, num)
        self.click_to_element(formatted_tariff)

    @allure.step('Ховер на кнопку информации о тарифе')
    def hover_to_information_tariff_button(self, num):
        formatted_button = self.format_locators(ChooseTariffPageLocators.TARIFF_INFORMATION_BUTTON, num)
        self.hover_over_element(formatted_button)

    @allure.step('Проверка отображения окна с информацией о тарифе')
    def check_visibility_of_information_tariff_popup(self, num):
        formatted_popup = self.format_locators(ChooseTariffPageLocators.TARIFF_INFORMATION_POPUP, num)
        return self.find_element_with_wait(formatted_popup)

    @allure.step('Проверка заголовка тарифа в окне с информацией о тарифе')
    def check_tariff_information_title(self, num):
        index = num + 1
        formatted_button = self.format_locators(ChooseTariffPageLocators.TARIFF_INFORMATION_TITLE, index)
        return self.get_text_from_element(formatted_button)

    @allure.step('Проверка описания тарифа в окне с информацией о тарифе')
    def check_tariff_information_description(self, num):
        index = num + 1
        formatted_button = self.format_locators(ChooseTariffPageLocators.TARIFF_INFORMATION_DESCRIPTION, index)
        return self.get_text_from_element(formatted_button)

    @allure.step('Выбор тарифа "Рабочий"')
    def click_to_work_tariff(self):
        work_locator = self.format_locators(ChooseTariffPageLocators.TARIFF_BUTTON, '1')
        self.click_to_element(work_locator)

    @allure.step('Получение стоимости поездки в тарифе "Рабочий"')
    def get_work_tariff_price(self):
        work_price_locator = self.format_locators(ChooseTariffPageLocators.TARIFF_PRICE, '1')
        return self.get_text_from_element(work_price_locator)

    @allure.step('Проверка отображения поля "Телефон"')
    def check_visibility_of_phone_input(self):
        return self.find_element_with_wait(ChooseTariffPageLocators.PHONE_INPUT)

    @allure.step('Проверка отображения поля "Способ оплаты"')
    def check_visibility_of_payment_option(self):
        return self.find_element_with_wait(ChooseTariffPageLocators.PAYMENT_OPTION_INPUT)

    @allure.step('Проверка отображения поля "Комментарий водителю"')
    def check_visibility_of_comment_input(self):
        return self.find_element_with_wait(ChooseTariffPageLocators.COMMENT_INPUT)

    @allure.step('Проверка отображения дропдауна "Требования к заказу"')
    def check_visibility_of_requirements_dropdown(self):
        return self.find_element_with_wait(ChooseTariffPageLocators.REQUIREMENTS_DROPDOWN)

    @allure.step('Проверка отображения кнопки "Ввести номер и заказать"')
    def check_visibility_of_order_submit_button(self):
        return self.find_element_with_wait(ChooseTariffPageLocators.ORDER_TAXI_SUBMIT_BUTTON)

    @allure.step('Проверка отображения блока с полями информации о заказе')
    def check_visibility_of_additional_fields(self):
        try:
            self.check_visibility_of_phone_input()
            self.check_visibility_of_payment_option()
            self.check_visibility_of_comment_input()
            self.check_visibility_of_requirements_dropdown()
            self.check_visibility_of_order_submit_button()
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False

    @allure.step('Открытие дропдауна "Требования к заказу"')
    def open_requirements_dropdown(self):
        self.click_to_element(ChooseTariffPageLocators.REQUIREMENTS_DROPDOWN_BUTTON)

    @allure.step('Выбор опции "Столик для ноутбука"')
    def click_to_laptop_switch(self):
        self.scroll_to_element(ChooseTariffPageLocators.LAPTOP_SWITCH)
        self.click_to_element(ChooseTariffPageLocators.LAPTOP_SWITCH)

    @allure.step('Клик на кнопку "Ввести номер и заказать"')
    def click_to_order_submit_button(self):
        self.click_to_element(ChooseTariffPageLocators.ORDER_TAXI_SUBMIT_BUTTON)

    @allure.step('Выбор тарифа "Рабочий", опции "Столик для ноутбука" и нажатие кнопки "Ввести номер и заказать"')
    def choose_tariff_requirements_and_click_submit_button(self):
        self.click_to_work_tariff()
        price = self.get_work_tariff_price()
        clean_price = HelpersMethods.clean_tariff_info_price(price)
        self.open_requirements_dropdown()
        self.click_to_laptop_switch()
        self.click_to_order_submit_button()
        return clean_price

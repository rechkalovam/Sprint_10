import allure
import data
from pages.base_page import BasePage
from locators.address_form_page_locators import AddressFormPageLocators


class AddressFormPage(BasePage):

    @allure.step('Ввод адреса точки А в поле "Откуда"')
    def add_point_a_to_address_form(self):
        self.add_text_to_element(AddressFormPageLocators.ADDRESS_FROM_INPUT, data.LOCATION_A)

    @allure.step('Ввод адреса точки B в поле "Куда"')
    def add_point_b_to_address_form(self):
        self.add_text_to_element(AddressFormPageLocators.ADDRESS_TO_INPUT, data.LOCATION_B)

    @allure.step('Ввод одинакового адреса в поля "Куда" и "Откуда"')
    def add_same_address_to_address_form(self):
        self.add_text_to_element(AddressFormPageLocators.ADDRESS_FROM_INPUT, data.LOCATION_A)
        self.add_text_to_element(AddressFormPageLocators.ADDRESS_TO_INPUT, data.LOCATION_A)

    @allure.step('Ввод двух разных адресов в поля "Куда" и "Откуда"')
    def add_addresses_to_address_form(self):
        self.add_point_a_to_address_form()
        self.add_point_b_to_address_form()
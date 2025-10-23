import allure
from selenium.common import TimeoutException
from helpers import HelpersMethods
from pages.base_page import BasePage
from locators.order_info_page_locators import OrderInfoPageLocators


class OrderInfoPage(BasePage):

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_block(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_WINDOW)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_title(self):
        return self.get_text_from_element(OrderInfoPageLocators.ORDER_TITLE)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_car_number(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_CAR_NUMBER)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_car_image(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_CAR_IMAGE)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_driver_photo(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_DRIVER_PHOTO)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_driver_rating(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_DRIVER_PHOTO)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_driver_name(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_DRIVER_NAME)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_cancel_button(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_CANCEL_BUTTON)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_details_button(self):
        return self.find_element_with_wait(OrderInfoPageLocators.ORDER_DETAILS_BUTTON)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_visibility_of_order_info_block_details(self):
        try:
            self.check_visibility_of_order_info_title()
            self.check_visibility_of_order_info_car_image()
            self.check_visibility_of_order_info_car_number()
            self.check_visibility_of_order_info_driver_photo()
            self.check_visibility_of_order_info_driver_rating()
            self.check_visibility_of_order_info_driver_name()
            self.check_visibility_of_order_info_cancel_button()
            self.check_visibility_of_order_info_details_button()
            return True
        except TimeoutException as e:
            print(f" Элемент не найден: {e}")
            return False

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def get_title_text_of_order_info_page(self):
        title = self.get_text_from_element(OrderInfoPageLocators.ORDER_TITLE)
        clean_title = HelpersMethods.clean_order_taxi_title(title)
        return clean_title

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def click_to_order_info_details_button(self):
        self.click_to_element(OrderInfoPageLocators.ORDER_DETAILS_BUTTON)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def get_order_price_to_order_details(self):
        price = self.get_text_from_element(OrderInfoPageLocators.ORDER_DETAILS_PRICE)
        clean_price = HelpersMethods.clean_order_info_price(price)
        return clean_price

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def click_to_order_info_cancel_button(self):
        self.click_to_element(OrderInfoPageLocators.ORDER_CANCEL_BUTTON)

    @allure.step('<UNK> <UNK> <UNK> <UNK> <UNK>')
    def check_invisibility_of_order_info_block(self):
        return self.wait_until_element_is_invisible(OrderInfoPageLocators.ORDER_WINDOW)

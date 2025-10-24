import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.waiting_order_page import WaitingOrderPage
from urls import URL_MAIN_PAGE
from pages.address_form_page import AddressFormPage
from pages.choose_route_page import ChooseRoutePage
from pages.choose_tariff_page import ChooseTariffPage
from pages.order_info_page import OrderInfoPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def fill_addresses(driver):
    address_form = AddressFormPage(driver)
    address_form.go_to_url(URL_MAIN_PAGE)
    address_form.add_addresses_to_address_form()
    choose_route_page = ChooseRoutePage(driver)
    return choose_route_page

@pytest.fixture()
def choose_tariff(driver, fill_addresses):
    fill_addresses.click_to_order_taxi_button()
    tariffs_block = ChooseTariffPage(driver)
    return tariffs_block

@pytest.fixture()
def order_taxi(driver, choose_tariff):
    price = choose_tariff.choose_tariff_requirements_and_click_submit_button()
    waiting_order_page = WaitingOrderPage(driver)
    return price, waiting_order_page

@pytest.fixture()
def finish_order(driver, order_taxi):
    price, waiting_order_page = order_taxi
    waiting_order_page.wait_until_waiting_order_timer_is_done()
    finish_order_page = OrderInfoPage(driver)
    return price, finish_order_page
import pytest
import sys
import allure
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from data import TARIFFS, TARIFFS_DESCRIPTION

class TestChooseTariffPage:

    @allure.title("Проверка отображения всех тарифов при нажатии кнопки 'Вызвать такси'")
    @pytest.mark.parametrize('tariff', TARIFFS)
    def test_order_taxi_form_displays_all_tariffs(self, choose_tariff, tariff):
        assert choose_tariff.check_visibility_of_tariffs(tariff), f'Тариф {tariff} не отображается'

    @allure.title("Проверка отображения активного тарифа при нажатии кнопки 'Вызвать такси'")
    def test_order_taxi_form_displays_active_tariff(self, choose_tariff):
        assert choose_tariff.check_visibility_of_active_tariff(), 'Активный тариф не отображается'

    @allure.title("Проверка отображения окна информации о тарифе при ховере на кнопку информации о тарифе")
    @pytest.mark.parametrize('num', range(6))
    def test_hover_tariff_information_button_displays_popup(self, choose_tariff, num):
        choose_tariff.click_to_tariff_button(num)
        choose_tariff.hover_to_information_tariff_button(num)
        tariff = TARIFFS[num]
        assert choose_tariff.check_visibility_of_information_tariff_popup(num), f'Тариф {tariff} не отображается'

    @allure.title("Проверка заголовка и описания тарифа в окне информации о тарифе")
    @pytest.mark.xfail(reason="Баг - Описания тарифов 'Сонный' и 'Разговорчивый' перепутаны между собой")
    @pytest.mark.parametrize('num, tariff, description', [(i, t, d) for i, (t, d) in enumerate(zip(TARIFFS, TARIFFS_DESCRIPTION))])
    def test_tariff_information_popup_display_correctly(self, choose_tariff, num, tariff, description):
        choose_tariff.click_to_tariff_button(num)
        choose_tariff.hover_to_information_tariff_button(num)
        assert choose_tariff.check_tariff_information_title(num) == tariff and choose_tariff.check_tariff_information_description(num) == description, \
            f'Заголовок тарифа: {tariff}, описание тарифа: {description}'

    @allure.title("Проверка отображения блока с полями об информации о заказе в блоке выбора тарифов")
    def test_order_taxi_form_displays_additional_fields(self, choose_tariff):
        assert choose_tariff.check_visibility_of_additional_fields(), 'Поле/я не отображается/ются'
import re


class HelpersMethods:
    @staticmethod
    def clean_tariff_info_price(text):
        return text.replace(' ₽', '').strip()

    @staticmethod
    def clean_order_info_price(text):
        return text.replace('Стоимость -', '').replace('₽', '').strip()

    @staticmethod
    def clean_order_taxi_title(text):
        return re.sub(r'\d+', 'n', text, count=1)
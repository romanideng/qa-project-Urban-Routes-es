from data import data
from pages.urban_routes_page import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)

    def test_1_set_route(self):
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_2_select_comfort(self):
        self.routes_page.step_select_comfort()

        comfort_tariff = self.routes_page.get_comfort_assert().text
        assert comfort_tariff == 'Comfort'

    def test_3_add_phone_number(self):
        self.routes_page.step_select_comfort()
        self.routes_page.step_phone_number(data.phone_number)

        phone_number = self.routes_page.get_phone_number_assert().text
        assert phone_number == data.phone_number

    def test_4_add_payment_method(self):
        self.routes_page.step_select_comfort()
        self.routes_page.step_add_card_payment(data.card_number, data.card_code)

        card_payment = self.routes_page.get_payment_assert().text
        assert card_payment == 'Tarjeta'

    def test_5_message_for_driver(self):
        self.routes_page.step_select_comfort()
        self.routes_page.step_comment_for_driver(data.message_for_driver)

        assert self.routes_page.get_comment_for_driver() == data.message_for_driver

    def test_6_click_blanket_switch(self):
        self.routes_page.step_select_comfort()
        self.routes_page.step_click_blanket_switch()

        assert self.routes_page.get_blanket_switch_assert()

    def test_7_add_ice_cream(self):
        self.routes_page.step_select_comfort()
        self.routes_page.step_add_ice_cream()

        assert self.routes_page.get_ice_cream_count().text == '2'

    def test_8_searching_taxi(self):
        self.routes_page.step_select_comfort()
        self.routes_page.step_phone_number(data.phone_number)
        self.routes_page.step_add_card_payment(data.card_number, data.card_code)
        self.routes_page.step_comment_for_driver(data.message_for_driver)
        self.routes_page.step_click_blanket_switch()
        self.routes_page.step_add_ice_cream()
        self.routes_page.step_click_request_smart_button()

        assert self.routes_page.get_searching_driver_window().text == 'Buscar automóvil'


    def test_9_wait_taxi_info(self):
        self.routes_page.step_select_comfort()
        self.routes_page.step_phone_number(data.phone_number)
        self.routes_page.step_add_card_payment(data.card_number, data.card_code)
        self.routes_page.step_comment_for_driver(data.message_for_driver)
        self.routes_page.step_click_blanket_switch()
        self.routes_page.step_add_ice_cream()
        self.routes_page.step_click_request_smart_button()
        self.routes_page.wait_for_searching_driver_window()
        driver_text = self.routes_page.get_searching_driver_window().text

        assert 'El conductor llegará en' in driver_text


   # def teardown_method(self):
       # self.driver.quit()

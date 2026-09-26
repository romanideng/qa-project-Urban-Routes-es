from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import data
from utils.retrieve_code import retrieve_phone_code


class UrbanRoutesPage:

    #LOCALIZADORES

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_number_button = (By.CSS_SELECTOR, '.np-button')
    phone_input = (By.ID, 'phone')
    phone_next_button = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    verification_code = (By.ID, 'code')
    confirm_code_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    phone_number_assert = (By.CSS_SELECTOR, '.np-button.filled .np-text')
    payment_button = (By.XPATH, '//div[@class="pp-text"]')
    add_card_button = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    card_number = (By.ID,'number')
    card_code = (By.CSS_SELECTOR, 'input.card-input#code')
    add_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    close_payment_window_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
    payment_assert = card_payment_assert = (By.CSS_SELECTOR, '.pp-value-text')
    comment_for_driver = (By.ID, 'comment')
    blanket_switch = (By.CSS_SELECTOR, '.switch .slider.round')
    blanket_switch_assert = (By.CSS_SELECTOR, '.switch-input')
    ice_cream_plus_button = (By.XPATH, '//div[text()="Helado"]/..//div[@class="counter-plus"]')
    ice_cream_count = (By.XPATH, '//div[text()="Helado"]/..//div[@class="counter-value"]')
    request_smart_button = (By.CSS_SELECTOR, '.smart-button')
    searching_driver_window = (By.CSS_SELECTOR, '.order-header-title')


    #FUNCIONES PARA OBTENER E INTERACTUAR CON LOS LOCALIZADORES
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

#1

    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')



#2

    def get_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_icon_assert)
        )



# 3
    def get_phone_number_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_phone_number(self, phone_input):
        self.wait.until(
            EC.visibility_of_element_located(self.phone_input)
        ).send_keys(phone_input)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_input).get_property('value')

    def get_phone_next_button(self):
        return self.driver.find_element(*self.phone_next_button)

    def click_phone_next_button(self):
        self.get_phone_next_button().click()

    def set_verification_code(self, verification_code):
        self.wait.until(
            EC.visibility_of_element_located(self.verification_code)
        ).send_keys(verification_code)

    def get_verification_code(self):
        return self.driver.find_element(*self.verification_code).get_property('value')

    def set_confirm_code_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.confirm_code_button)
        )

    def get_confirm_code_button(self):
        return self.driver.find_element(*self.confirm_code_button)

    def click_confirm_code_button(self):
        self.get_confirm_code_button().click()

    def get_phone_number_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.phone_number_assert)
        )


#4
    def get_payment_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.payment_button)
        )

    def click_payment_button(self):
        self.get_payment_button().click()

    def get_add_card_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def set_card_number(self, card_number):
        self.wait.until(
            EC.visibility_of_element_located(self.card_number)
        ).send_keys(card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def set_card_code(self, card_code):
        self.wait.until(
            EC.visibility_of_element_located(self.card_code)
        ).send_keys(card_code)

    def get_card_code(self):
        return self.driver.find_element(*self.card_code).get_property('value')

    def press_tab_key(self):
        self.wait.until(
            EC.visibility_of_element_located(self.card_code)
        ).send_keys(Keys.TAB)

    def get_add_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_button)
        )

    def click_add_button(self):
        self.get_add_button().click()

    def get_close_payment_method_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.close_payment_window_button)
        )

    def click_close_payment_method_button(self):
        self.get_close_payment_method_button().click()

    def get_payment_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.payment_assert)
        )

#5

    def set_comment_for_driver(self, comment_for_driver):
        self.wait.until(
            EC.visibility_of_element_located(self.comment_for_driver)
        ).send_keys(comment_for_driver)

    def get_comment_for_driver(self):
        return self.driver.find_element(*self.comment_for_driver).get_property('value')


    #6

    def get_blanket_switch(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.blanket_switch)
        )

    def click_blanket_switch(self):
        self.get_blanket_switch().click()

    def get_blanket_switch_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.blanket_switch_assert)
        ).is_selected()


#7
    def get_ice_cream_plus_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.ice_cream_plus_button)
        )
    def click_ice_cream_plus_button(self):
        self.get_ice_cream_plus_button().click()

    def get_ice_cream_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ice_cream_count)
        )

    def set_ice_cream_count(self, count):
        for _ in range(count):
            self.click_ice_cream_plus_button()


#8
    def get_request_smart_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_smart_button)
        )

    def click_request_smart_button(self):
        self.get_request_smart_button().click()

    def get_searching_driver_window(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.searching_driver_window)
        )

    def wait_for_searching_driver_window(self):
        return WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(self.searching_driver_window, "El conductor llegará en")
        )

    def get_driver_info(self):
        return self.get_searching_driver_window()


# STEP_BY_STEP

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def step_select_comfort(self):
        self.click_request_taxi_button()
        self.click_comfort_icon()

    def step_phone_number(self,phone_number):
        self.click_phone_number_button()
        self.set_phone_number(phone_number)
        self.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.set_verification_code(code)
        self.click_confirm_code_button()

    def step_add_card_payment(self, card_number, card_code):
        self.click_payment_button()
        self.click_add_card_button()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.press_tab_key()
        self.click_add_button()
        self.click_close_payment_method_button()

    def  step_comment_for_driver(self, comment_for_driver):
        self.set_comment_for_driver(comment_for_driver)

    def step_click_blanket_switch(self):
        self.click_blanket_switch()

    def step_add_ice_cream(self):
        self.set_ice_cream_count(2)

    def step_click_request_smart_button(self):
        self.click_request_smart_button()



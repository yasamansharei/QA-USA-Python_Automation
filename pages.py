from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import helpers
from helpers import retrieve_phone_code


# Create a class for both tests
class UrbanRoutesPage:
        # Route fields (IDs exist)
        FROM_LOCATOR = (By.ID, 'from')
        TO_LOCATOR = (By.ID, 'to')

        # Call taxi button (text-based)
        CALL_A_TAXI_LOCATOR = (By.XPATH, '//button[text()="Call a taxi"]')

        # Tariff cards / selected plan
        SUPPORTIVE_LOCATOR = (By.XPATH, '//div[contains(@class,"tcard")][.//div[text()="Supportive"]]')
        SUPPORTIVE_ACTIVE_LOCATOR = (By.XPATH,"//div[contains(@class,'tcard') and contains(@class,'active')][.//div[text()='Supportive']]")

        # Phone flow
        PHONE_NUMBER_LOCATOR = (By.CSS_SELECTOR, ".np-button")
        PHONE_NUMBER_ENTER_LOCATOR = (By.ID, "phone")
        PHONE_NUMBER_NEXT_LOCATOR = (By.XPATH, '//button[text()="Next"]')
        PHONE_CODE_LOCATOR = (By.ID, 'code')
        CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[contains(normalize-space(.), 'Confirm')]")
        SMS_INPUT_LOCATOR = (By.ID, "code")

        # Payment / card flow
        PAYMENT_METHOD_LOCATOR =(By.CSS_SELECTOR, '.pp-button')
        ADD_A_CARD_LOCATOR = (By.CSS_SELECTOR, '.pp-plus')
        CARD_NUMBER_LOCATOR = (By.ID, 'number')
        CVV_CODE_LOCATOR = (By.XPATH, '//*[@id="code" and @class="card-input"]')
        LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
        PAYMENT_METHOD_TEXT = (By.CLASS_NAME, 'pp-value-text')


        # Driver comment
        COMMENT_LOCATOR = (By.ID, 'comment')

        # Blanket & handkerchief toggles -> click the slider element
        BLANKET_LOCATOR = (By.XPATH, '//div[contains(@class,"sw")][.//div[text()="Blanket and handkerchiefs"]]//span[contains(@class,"slider")]')
        BLANKET_CHECKED_LOCATOR = (By.XPATH, '//div[contains(@class,"sw")][.//div[normalize-space()="Blanket and handkerchiefs"]]//input[@type="checkbox"]')

        # Ice cream controls: plus button and counter value
        ICECREAM_ADD_LOCATOR = (By.XPATH, '//div[text()="+"]')
        ORDER_A_TAXI_LOCATOR = (By.XPATH, '//button[.//span[text()="Enter the number and order"]]')
        CAR_SEARCH_LOCATOR = (By.XPATH, '//div[@class = "order-body"]')
        ICECREAM_NUMBER_CHECK = (By.XPATH, "//div[contains(@class,'counter-container')][.//div[normalize-space(text())='Ice cream']]//div[contains(@class,'counter-value')]")


        def __init__(self, driver):
            self.driver = driver  # Initialize the driver

        #  Route
        def enter_from_location(self, from_text):
            # Enter From
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FROM_LOCATOR)).send_keys(from_text)

        def get_from_location(self):
            return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

        def enter_to_location(self, to_text):
            # Enter To
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TO_LOCATOR)).send_keys(to_text)

        def get_to_location(self):
            return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

        # Call A taxi
        def click_call_a_taxi(self):
            # Click Call a taxi
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CALL_A_TAXI_LOCATOR)).click()

        #  Plan
        def click_supportive(self):
             WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.SUPPORTIVE_LOCATOR)).click()


        def get_supportive_option(self):
            return self.driver.find_element(*self.SUPPORTIVE_LOCATOR).text

        # Phone
        def click_phone_number(self):
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.PHONE_NUMBER_LOCATOR)).click()

        def click_enter_phone_number(self):
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.PHONE_NUMBER_ENTER_LOCATOR)).click()

        def enter_phone_number(self, phone_number):
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.PHONE_NUMBER_ENTER_LOCATOR)).send_keys(phone_number)

        def click_next_phone_number(self):
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.PHONE_NUMBER_NEXT_LOCATOR)).click()

        def enter_sms_code(self, code):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SMS_INPUT_LOCATOR)).send_keys(code)

        def click_confirm_phone(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONFIRM_BUTTON_LOCATOR)).click()

        def wait_for_sms_code(self) -> str:
            code = helpers.retrieve_phone_code(self.driver)
            return code

        def get_phone_number(self):
            return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).text

        # Payment
        def click_payment_method(self):
            self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

        def click_add_a_card(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_A_CARD_LOCATOR)).click()

        def enter_card_number(self, card_number):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CARD_NUMBER_LOCATOR)).send_keys(card_number)

        def enter_cvv_code(self, cvv_code):
             WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CVV_CODE_LOCATOR)).send_keys(cvv_code)

        def click_link_button(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CVV_CODE_LOCATOR)).send_keys(Keys.TAB)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LINK_BUTTON_LOCATOR)).click()


        def get_payment_method(self):
            return self.driver.find_element(*self.PAYMENT_METHOD_TEXT).text

        def enter_comment(self, comment):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.COMMENT_LOCATOR)).send_keys(comment)

        def get_comment_text(self):
            return self.driver.find_element(*self.COMMENT_LOCATOR).get_attribute("value")

        def choose_blanket_and_handkerchiefs(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BLANKET_LOCATOR)).click()

        def is_blanket_selected(self):
            return self.driver.find_element(*self.BLANKET_CHECKED_LOCATOR).get_attribute("checked")

        def click_icecream(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ICECREAM_ADD_LOCATOR)).click()

        def check_icecream(self):
            return self.driver.find_element(*self.  ICECREAM_NUMBER_CHECK).text


        def choose_order_a_taxi(self):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_A_TAXI_LOCATOR)).click()

        def is_car_search_shown(self):
            self.driver.find_element(*self.CAR_SEARCH_LOCATOR).is_displayed()

        def enter_locations(self, from_text, to_text):
            self.enter_from_location(from_text)
            self.enter_to_location(to_text)

        def fill_phone_number(self, phone_number):
            self.click_phone_number()
            self.enter_phone_number(phone_number)
            self.click_next_phone_number()


        def fill_payment_method(self, card_number, cvv_code):
            self.click_payment_method()
            self.click_add_a_card()
            self.enter_card_number(card_number)
            self.enter_cvv_code(cvv_code)
            self.click_link_button()
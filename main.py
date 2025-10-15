from selenium import webdriver
import data
import helpers
import time
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        """
        This method runs once before all tests in this class.
        It checks whether the Urban Routes server is reachable.
        """
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8: Implement the steps for setting a route
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        from_value = urban_routes_page.get_from_location()
        to_value = urban_routes_page.get_to_location()
        expected_value_from= "East 2nd Street, 601"
        expected_value_to = "1300 1st St"
        assert from_value == expected_value_from
        assert to_value == expected_value_to


    def test_select_plan(self):
        # Add in S8: Implement the steps for selecting a plan
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        actual_value = urban_routes_page.get_supportive_option()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"


    def test_fill_phone_number(self):
        # Add in S8: Implement the steps for filling in a phone number
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        code = urban_routes_page.wait_for_sms_code()
        time.sleep(2)
        urban_routes_page.enter_sms_code(code)
        urban_routes_page.click_confirm_phone()
        actual_phone = urban_routes_page.get_phone_number()
        assert data.PHONE_NUMBER == actual_phone, f"Expected '{data.PHONE_NUMBER}', got '{actual_phone}'"


    def test_fill_card(self):
        # Add in S8: Implement the steps for filling in a card
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        urban_routes_page.fill_payment_method(data.CARD_NUMBER, data.CARD_CODE)
        actual_value = urban_routes_page.get_payment_method()
        assert "Card" in actual_value, f"Expected 'Card', got '{actual_value}'"


    def test_comment_for_driver(self):
        # Add in S8: Implement the steps for adding a comment for the driver
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        actual_comment = urban_routes_page.get_comment_text()
        assert data.MESSAGE_FOR_DRIVER == actual_comment, f"Expected '{data.MESSAGE_FOR_DRIVER}', got '{actual_comment}'"


    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8: Implement the steps for ordering blanket and handkerchiefs
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        urban_routes_page.choose_blanket_and_handkerchiefs()
        assert urban_routes_page.is_blanket_selected()

    def test_order_2_ice_creams(self):
        # Loop twice since the requirement is to order 2 ice creams
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        int(urban_routes_page.check_icecream())
        for _ in range(2):
            urban_routes_page.click_icecream()
            time.sleep(0.3)

        assert int(urban_routes_page.check_icecream()) == 2


    def test_car_search_model_appears(self):
        # Add in S8: Implement the steps for verifying car search model appears
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.is_car_search_shown()




@classmethod
def teardown_class(cls):
    cls.driver.quit()
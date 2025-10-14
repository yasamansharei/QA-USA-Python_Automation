from selenium import webdriver
import data
import helpers
import time
from pages import UrbanRoutesPage
BASE_URL = "https://cnt-f8358816-ed11-44f2-9efb-fb808816b81a.containerhub.tripleten-services.com/"

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
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        from_value = urban_routes_page.get_from_location()
        to_value = urban_routes_page.get_to_location()
        expected_value_from= "East 2nd Street, 601"
        expected_value_to = "1300 1st St"
        assert from_value == expected_value_from
        assert to_value == expected_value_to
        print("function created for set_route")
        pass

    def test_select_plan(self):
        # Add in S8: Implement the steps for selecting a plan
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_supportive()
        time.sleep(2)
        actual_value = urban_routes_page.get_supportive_option()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8: Implement the steps for filling in a phone number
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_supportive()
        time.sleep(2)
        urban_routes_page.fill_phone_number("+1 310 922 9411")
        expected_phone = "+1 310 922 9411"
        actual_phone = urban_routes_page.fill_phone_number("+1 310 922 9411")
        print("Function created for fill_phone_number")
        pass

    def test_fill_card(self):
        # Add in S8: Implement the steps for filling in a card
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        urban_routes_page.click_call_a_taxi()
        urban_routes_page.click_supportive()
        urban_routes_page.fill_payment_method("1234 0000 4321", "12")
        actual_value = urban_routes_page.get_payment_method()
        assert "Card" in actual_value, f"Expected 'Card', got '{actual_value}'"
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8: Implement the steps for adding a comment for the driver
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_supportive()
        time.sleep(2)
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        actual_comment = urban_routes_page.get_comment_text()
        assert data.MESSAGE_FOR_DRIVER == actual_comment, f"Expected '{data.MESSAGE_FOR_DRIVER}', got '{actual_comment}'"
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8: Implement the steps for ordering blanket and handkerchiefs
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_supportive()
        time.sleep(2)
        urban_routes_page.choose_blanket_and_handkerchiefs()
        assert urban_routes_page.is_blanket_selected()
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Loop twice since the requirement is to order 2 ice creams
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_supportive()
        time.sleep(2)
        int(urban_routes_page.check_icecream())
        for _ in range(2):
            urban_routes_page.click_icecream()
            time.sleep(0.3)

        assert int(urban_routes_page.check_icecream()) == 2
        print("function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8: Implement the steps for verifying car search model appears
        self.driver.get(BASE_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        time.sleep(2)
        urban_routes_page.click_call_a_taxi()
        time.sleep(2)
        urban_routes_page.click_supportive()
        time.sleep(2)
        urban_routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.is_car_search_shown()
        print("function created for car search model")
        pass



@classmethod
def teardown_class(cls):
    cls.driver.quit()
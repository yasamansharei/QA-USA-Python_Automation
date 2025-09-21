import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
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
        print("function created for set_route")
        pass

    def test_select_plan(self):
        # Add in S8: Implement the steps for selecting a plan
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8: Implement the steps for filling in a phone number
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8: Implement the steps for filling in a card
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8: Implement the steps for adding a comment for the driver
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8: Implement the steps for ordering blanket and handkerchiefs
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Loop twice since the requirement is to order 2 ice creams
        for i in range(2):
            # Add in S8: Add logic for ordering one ice cream here
            pass

        # Final check or step after ordering 2 ice creams
        print("function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8: Implement the steps for verifying car search model appears
        print("function created for car search model")
        pass

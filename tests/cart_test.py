from tests.base_test import BaseTest


class CartTestNo1(BaseTest):
    """
    Adding to cart TEST
    """

    def setUp(self):
        super().setUp()
        # STEPS OF THE SETUP:
        # 1. Disable cookies
        self.home_page.cookie_button_click()
        # 2. Find and click side menu
        self.home_page.open_side_menu()
        # 3. Find and click on "szklo spectrum", go to spectrum_page
        self.home_page.open_spectrum_page()
        # 4. Choose "on stock" option
        self.spectrum_page.select_on_stock()

    def test_add_to_cart(self):
        # STEPS OF THE TEST:
        # 1. Information about commencing the test
        print("Start of the test No.1: test_add_to_cart")
        # 2. Choose first item for sale and add to cart
        self.spectrum_page.choose_first_item_and_add_to_cart()
        # 3. Click on "go to cart"
        self.spectrum_page.go_to_cart()
        # 4. Check if message "1 produkt" is displayed
        self.assertEqual('1 produkt', self.cart_page.get_no_of_items_upper_message())
        # 5. Check if item price is equal to final item/s price
        self.assertEqual(self.cart_page.get_item_price(), self.cart_page.get_total_price())
        # 6.Information about the end of the test
        print("End of the test No.1: test_add_to_cart")


class CartTestNo2(BaseTest):
    """
    Multiplying item already present in the cart TEST
    """

    def setUp(self):
        super().setUp()
        # STEPS OF THE SETUP:
        # 1. Disable cookies
        self.home_page.cookie_button_click()
        # 2. Find and click side menu
        self.home_page.open_side_menu()
        # 3. Find and click on "szklo spectrum", go to spectrum_page
        self.home_page.open_spectrum_page()
        # 4. Choose "on stock" option
        self.spectrum_page.select_on_stock()
        # 5. Choose first item for sale and add to cart
        self.spectrum_page.choose_first_item_and_add_to_cart()
        # 6. Click on "go to cart"
        self.spectrum_page.go_to_cart()

    def test_add_additional_object_to_cart(self):
        # STEPS OF THE TEST:
        # 1. Information about commencing the test
        print("Start of the test No.2: test_add_additional_object_to_cart")
        # 2. Click on "plus icon" randomly (from 1 to 3 times) and check if total price was increased correctly
        click_times = self.cart_page.click_plus_icon_randomly()
        self.cart_page.compare_total_price_after_plus_click(click_times)
        # 3. Check if information about number of items in cart is the same
        #    in the table as well as in message for the costumer
        self.assertEqual(self.cart_page.get_total_number_of_items_in_cart_from_upper_corner(),
                         self.cart_page.get_number_of_items_in_cart_from_table())
        # 4. Information about the end of the test
        print("End of the test No.2: test_add_additional_object_to_cart")


class CartTestNo3(BaseTest):
    """
    Reducing number of items in cart, but not all of them TEST
    """

    def setUp(self):
        super().setUp()
        # STEPS OF THE SETUP:
        # 1. Disable cookies
        self.home_page.cookie_button_click()
        # 2. Find and click side menu
        self.home_page.open_side_menu()
        # 3. Find and click on "szklo spectrum", go to spectrum_page
        self.home_page.open_spectrum_page()
        # 4. Choose "on stock" option
        self.spectrum_page.select_on_stock()
        # 5. Choose first item for sale and add to cart
        self.spectrum_page.choose_first_item_and_add_to_cart()
        # 6. Click on "go to cart"
        self.spectrum_page.go_to_cart()
        # 7. Click on "plus icon" randomly (from 1 to 3 times) and check if total price was increased correctly
        self.cart_page.click_plus_icon_randomly()

    def test_substract_some_objects_from_cart(self):
        # STEPS OF THE TEST:
        # 1. Information about commencing the test
        print("Start of the test No.3: test_substract_some_objects_from_cart")
        # 2. Click on "minus icon" randomly (from 1 to 3 times) and check if total price was decreased correctly
        self.cart_page.click_minus_icon_randomly()
        self.cart_page.compare_total_price_after_minus_click()
        # 3. Check if information about number of items in cart is the same
        #    in the table as well as in message for the costumer
        self.assertEqual(self.cart_page.get_total_number_of_items_in_cart_from_upper_corner(),
                         self.cart_page.get_number_of_items_in_cart_from_table())
        # 4. Information about the end of the test
        print("End of the test No.3: test_substract_some_objects_from_cart")


class CartTestNo4(BaseTest):
    """
    Removing all items frm cart TEST
    """

    def setUp(self):
        super().setUp()

    def test_substract_all_objects_from_cart(self):
        # KROKI
        # 1. Information about commencing the test
        print("Start of the test No.4: test_substract_all_objects_from_cart")
        # 2. Disable cookies
        self.home_page.cookie_button_click()
        # 3. Find and click side menu
        self.home_page.open_side_menu()
        # 4. Find and click on "szklo spectrum", go to spectrum_page
        self.home_page.open_spectrum_page()
        # 5. Choose "on stock" option
        self.spectrum_page.select_on_stock()
        # 6. Choose first item for sale and add to cart
        self.spectrum_page.choose_first_item_and_add_to_cart()
        # 7. Click on "go to cart"
        self.spectrum_page.go_to_cart()
        # 8. Click on "trashcan icon"
        self.cart_page.click_trash_icon()
        # 9. Check if message about empty cart is displayed
        self.assertEqual('Twój koszyk jest pusty.', self.cart_page.get_empty_cart_message())
        # 10. Information about the end of the test
        print("End of the test No.4: test_substract_all_objects_from_cart")

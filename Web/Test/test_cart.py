import time

import allure
import pytest
from Web.Page.cart_page import Cart_page



class Test_cart():
    @allure.description('Verify all the user interface in the page ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_homepage(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        assertion_text = cart.carts_ball_go
        assert assertion_text == "מבצעים"

    @allure.description('First, verify whether add to cart button is clickable or not. ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_button(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_product()
        cart.click_on_radio_plus_button()
        assertion_text = cart.carts_ball_plus
        assert assertion_text == "בדיקה חדשה 1"

    @allure.description('Check whether the user is able to add the item to the cart or not.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_user_able_to_add_item_to_cart(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_product()
        cart.click_on_radio_plus_button()
        cart.click_on_radio_minus_button()
        assertion_text = cart.carts_ball_plus
        assert assertion_text == "בדיקה חדשה 1"


    @allure.description('Verify that the count of the cart getting changing or not when the user adds an item to the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_get_change(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_product()
        cart.click_on_radio_plus_button()
        cart.click_on_sumtotal_button()
        assertion_text = cart.carts_ball_plus
        assert assertion_text == "בדיקה חדשה 1"


    @allure.description('Check that when the user tries to add the same item to the cart multiple times.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_add_same_item_to_cart(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_radio_plus_button()
        assertion_text = cart.carts_ball_plus_add
        assert assertion_text == '₪578.00'

    @allure.description('Check that count of the cart gets changed  when the user clicks on add to cart button for the second time.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_count_of_cart_gets_change_when_user_clicking_second_time(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_radio_plus_button()
        cart.click_on_sumtotal_button()
        assertion_text = cart.carts_ball_plus_add
        assert assertion_text == '₪578.00'


    @allure.description('Verify that the item added to the cart shows the same item as clicking on add to cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_Verify_that_the_item_added_to_the_cart_shows_the_same_item(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        assertion_text = cart.carts_ball_same
        assert assertion_text == "אקדיה"

    @allure.description('Verify the count of the cart showing properly when the user adds any item to the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_sumtotal_button()
        assertion_text = cart.carts_ball_same
        assert assertion_text == "אקדיה"

    @allure.description('Check that user is able to remove or delete items from the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_delete_items(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_delete_button()
        assertion_text = cart.carts_ball_delete
        assert assertion_text == "העגלה שלך ריקה"

    @allure.description('Check that all the items added to the cart showing in proper sequence.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_proper_sequence(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_checkout_buttons()
        assertion_text = cart.carts_ball_sequence
        assert assertion_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"

    @allure.description('Check that when the user tries to checkout only one item from the cart')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_checkout(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_checkout_buttons()
        assertion_text = cart.carts_ball_sequence
        assert assertion_text == "ברוכים השבים! מתרגשים לראות אתכם כאן"

    @allure.description('Check that subtotal of all items in the cart shows the exact amount or not.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_exact_amount(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_checkout_buttons()
        assertion_text = cart.carts_ball_excat_amount
        assert assertion_text == "289.00₪"

    @allure.description('Check whether the subtotal is getting changed or not when the user removes any item from the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_subtotal_changed(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_delete_button()
        assertion_text = cart.carts_ball_excat_amount
        assert assertion_text == "289.00₪"

    @allure.description('Verify that the user is able to change the number of items from the cart or not.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_change_the_no(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_radio_minus_button()
        assertion_text = cart.carts_ball_excat_amount
        assert assertion_text == "289₪"

    @allure.description('Check details description page getting open or not when the user clicks on the item name from the cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_details(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        assertion_text = cart.carts_ball_excat_amount
        assert assertion_text == "289.00₪"

    @allure.description('Verify by adding the multiple products and check the calculations total and subtotal are correct')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_multiple(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        assertion_text = cart.carts_ball_multiple
        assert assertion_text == "₪33.81"

    @allure.description('Verify any minimum quantity rules/restrictions')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_quantity(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the shopping cart icon is displayed as expected or not.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_shopping(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Verify whether the shopping cart page UI should be as expected')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_shopping_cart(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the Add to Cart icon is seen on the product detail page.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_Cart_icon(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the item is added to the cart when clicking on the button')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_clicking(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the item added to the cart shows the same item as clicking on add to cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_cart_shows(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the quantity button is displayed as expected.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_quantity_button(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the ‘+’ and ‘-‘ button is seen on the shopping cart page.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_button(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the same product is added to the cart along with an increase in the corresponding cost in the total price when clicking on the ‘+’ button.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_same_product(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the cart becomes empty when the user clicks on the ‘-‘ button when only a single product is present in the shopping cart.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_empty(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_product()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether the shopping cart page has options for edit, delete etc')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_option(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_on_radio_minus_button()
        cart.click_delete_button()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Check whether that Proceed button works properly')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_properly(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()
        cart.click_on_radio_plus_button()
        cart.click_checkout_buttons()
        assertion_text = cart.carts_ball
        assert assertion_text == ""

    @allure.description('Verify product images are displaying properly')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_cart_page_image(self):
        cart = Cart_page(self)
        cart.open_website()
        cart.click_option1()
        cart.click_option2()
        cart.click_save_button()
        cart.click_on_sample_product_button()










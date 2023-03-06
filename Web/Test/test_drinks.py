import time

import allure
import pytest
from Web.Page.drinks_page import Drink_page



class Test_canabis():

    @allure.description('Verify all the user interface in the Page ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_canabis_page(self):
        sales = Drink_page(self)
        sales.open_trado()
        sales.click_option1()
        sales.click_option2()
        sales.click_save_button()
        sales.click_on_drinks_page()
        assertion_text = sales.drinks_assertion
        assert "משקאות" == assertion_text

    @allure.description('Test if the sort with lowest price')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_sort_lowest_price(self):
        lowest = Drink_page(self)
        lowest.open_trado()
        lowest.click_option1()
        lowest.click_option2()
        lowest.click_save_button()
        lowest.click_on_drinks_page()
        lowest.sort_by_lowest_price()
        assertion_text = lowest.lower_price_assertion
        assert "9990.00₪" == assertion_text
        lowest.second_lowest_price_assertion()

    @allure.description('Test if the sort with highest price')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_sort_higest_price(self):
        lowest = Drink_page(self)
        lowest.open_trado()
        lowest.click_option1()
        lowest.click_option2()
        lowest.click_save_button()
        lowest.click_on_drinks_page()
        lowest.sort_by_highest_price()
        assertion_text = lowest.highest_price_assertion
        assert "10000.00₪" == assertion_text

    @allure.description('Test if the sort with popularity price')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_sort_popularity_price(self):
        lowest = Drink_page(self)
        lowest.open_trado()
        lowest.click_option1()
        lowest.click_option2()
        lowest.click_save_button()
        lowest.click_on_drinks_page()
        lowest.sort_by_popularity()
        assertion_text = lowest.popularity_price_assertion
        assert "goats milk" == assertion_text


    @allure.description('Test if the product is displayed as list')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_displayed_as_list(self):
        lists = Drink_page(self)
        lists.open_trado()
        lists.click_option1()
        lists.click_option2()
        lists.click_save_button()
        lists.click_on_drinks_page()
        lists.click_on_landscape_view()


    @allure.description('Test if the product is displayed as grid')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_displayed_as_grid(self):
        lists = Drink_page(self)
        lists.open_trado()
        lists.click_option1()
        lists.click_option2()
        lists.click_save_button()
        lists.click_on_drinks_page()
        lists.click_on_grid_view()

    @allure.description('Test if the product opens by clicking')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_product(self):
        product = Drink_page(self)
        product.open_trado()
        product.click_option1()
        product.click_option2()
        product.click_save_button()
        product.click_on_drinks_page()
        product.click_on_product_milk()
        assertion_text = product.drinks_assertion
        assert "Milk" == assertion_text

    @allure.description('Test if the product opens and adding button (+) works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_product_add(self):
        product = Drink_page(self)
        product.open_trado()
        product.click_option1()
        product.click_option2()
        product.click_save_button()
        product.click_on_drinks_page()
        product.click_on_product_milk()
        product.click_on_product_milk_plus()
        assertion_text = product.add_product_assertion
        assert "₪514,285.20" == assertion_text

    @allure.description('Test if the product opens and adding button (-) works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_product_minus(self):
        product = Drink_page(self)
        product.open_trado()
        product.click_option1()
        product.click_option2()
        product.click_save_button()
        product.click_on_drinks_page()
        product.click_on_product_milk()
        product.click_on_product_milk_minus()
        assertion_text = product.minus_product_assertion
        assert "העגלה שלך ריקה" == assertion_text

    @allure.description('Test_login_with_valid_credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_the_clickability_of_uses_link(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_on_for_uses_side_bar_link()

    @allure.description('test_the_clickability_of_common_question_link')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_the_clickability_of_common_question_link(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_common_questionslink()


    @allure.description('test_the_clickability_of_contact_us_link')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_the_clickability_of_contact_us_link(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()

    @allure.description('test_the_clickability_of_how_dekivery_works_link')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_the_clickability_of_how_dekivery_works_link(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_how_delivery_workslink()

    @allure.description('test_sending_message_from_contact_us_page_by_filling_all_valid_credintials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_by_filling_all_valid_credintials(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("Getachew")
        sidebar.setting_last_name_on_contact_us("Gessesse")
        sidebar.setting_gmail_contact_us("Test@gmail.com")
        sidebar.setting_phone_contact_us("0534231334")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()
        sidebar.assertion_valid_message()

    @allure.description('test_sending_message_from_contact_us_page_without_filling_all_valid_credintials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_without_filling_all_valid_credintials(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.click_on_send_button()
        sidebar.setting_gmail_contact_us("qwer")
        sidebar.null_message_assertion()

    @allure.description('test_sending_message_from_contact_us_page_without_filling_gmail_field_credintials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_without_filling_gmail_field_credintials(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("Getachew")
        sidebar.setting_last_name_on_contact_us("Gessesse")
        sidebar.setting_gmail_contact_us("")
        sidebar.setting_phone_contact_us("0534231334")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()
        sidebar.null_email_assertion()

    @allure.description('test_sending_message_from_contact_us_page_without_filling_first_last_name_fields_credintials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_without_filling_first_last_name_fields_credintials(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("")
        sidebar.setting_last_name_on_contact_us("")
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        sidebar.setting_phone_contact_us("0534231334")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()
        sidebar.null_email_assertion()

    @allure.description('test_sending_message_from_contact_us_page_without_filling_telephone_fields_credintials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_without_filling_telephone_fields_credintials(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("asdf")
        sidebar.setting_last_name_on_contact_us("qwer")
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        sidebar.setting_phone_contact_us("")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()

    @allure.description('test_sending_message_from_contact_us_page_with_filling_invalid_email_credintials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_with_filling_invalid_email_credintials(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("asdf")
        sidebar.setting_last_name_on_contact_us("qwer")
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        sidebar.setting_phone_contact_us("")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()

    @allure.description('test_sending_message_from_contact_us_page_with_filling_less_than_10_digit_phone')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_with_filling_less_than_10_digit_phone(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("asdf")
        sidebar.setting_last_name_on_contact_us("qwer")
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        sidebar.setting_phone_contact_us("05433421")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()

    @allure.description('test_sending_message_from_contact_us_page_with_filling_more_than_10_digit_phone')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_with_filling_more_than_10_digit_phone(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("asdf")
        sidebar.setting_last_name_on_contact_us("qwer")
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        sidebar.setting_phone_contact_us("05433421123456")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()

    @allure.description('test_sending_message_from_contact_us_page_with_filling_string_digit_phone')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_with_filling_string_digit_phone(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("asdf")
        sidebar.setting_last_name_on_contact_us("qwer")
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        sidebar.setting_phone_contact_us("adsfgdgdvdb")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()

    @allure.description('test_sending_message_from_contact_us_page_with_filling_special_character_digit_phone')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_with_filling_special_character_digit_phone(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("asdf")
        sidebar.setting_last_name_on_contact_us("qwer")
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        sidebar.setting_phone_contact_us("!@#$%^&*()_+")
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        sidebar.click_on_send_button()

    @allure.description('test_sending_message_from_contact_us_page_by_filling_more_than_100_characters_on_message_field')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_by_filling_more_than_100_characters_on_message_field(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("Getachew")
        sidebar.setting_last_name_on_contact_us("Gessesse")
        sidebar.setting_gmail_contact_us("Test@gmail.com")
        sidebar.setting_phone_contact_us("0534231334")
        sidebar.setting_message_contact_us(
            "Hi there, this is getachew cbncvbcvhgsahgfhagsg   ghscgshcgchsc gvchscvshcsva bmsncbhcvjavhcajcvhajcvavchsgcasjchvsjcgvjhcscjjscvja"
            "nxbz nxzb nzxb zxzzxcbjsdvdsv jhbdsjhbdskvbdsvjdsbvkdsjvbksdvdskvbjdsvdjskvbdsvs,v dsdsvdsbdsjvkshgcvsjc")
        time.sleep(1)
        sidebar.click_on_send_button()
        sidebar.assertion_valid_message()

    @allure.description('test_sending_message_from_contact_us_page_by_filling_less_than_100_characters_on_message_field')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_sending_message_from_contact_us_page_by_filling_less_than_100_characters_on_message_field(self):
        sidebar = Drink_page(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        sidebar.click_for_contact_us_link()
        sidebar.setting_first_name_on_contact_us("Getachew")
        sidebar.setting_last_name_on_contact_us("Gessesse")
        sidebar.setting_gmail_contact_us("Test@gmail.com")
        sidebar.setting_phone_contact_us("0534231334")
        sidebar.setting_message_contact_us("Hi there, this is getachew cbncvbcvhgsac")
        sidebar.click_on_send_button()
        sidebar.assertion_valid_message()

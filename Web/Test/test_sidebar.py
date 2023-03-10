import pytest
from Web.Page.sidebar_page import SideBar
import time
import allure



class Test_Sidebar:

    @allure.description('Test_login_with_valid_credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_the_clickability_of_uses_link(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(6)
        sidebar.click_on_for_uses_side_bar_link()
        time.sleep(7)

    def test_the_clickability_of_common_question_link(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(6)
        sidebar.click_for_common_questionslink()
        time.sleep(7)

    def test_the_clickability_of_contact_us_link(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)

    def test_the_clickability_of_how_dekivery_works_link(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_how_delivery_workslink()
        time.sleep(2)

    def test_sending_message_from_contact_us_page_by_filling_all_valid_credintials(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("Getachew")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("Gessesse")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("test@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("0534231334")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()
        sidebar.assertion_valid_message()

    def test_sending_message_from_contact_us_page_without_filling_all_valid_credintials(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.click_on_send_button()
        sidebar.setting_gmail_contact_us("qwer")
        sidebar.null_message_assertion()


    def test_sending_message_from_contact_us_page_without_filling_gmail_field_credintials(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("Getachew")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("Gessesse")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("")
        time.sleep(1)
        sidebar.setting_phone_contact_us("0534231334")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()
        time.sleep(6)
        sidebar.null_email_assertion()


    def test_sending_message_from_contact_us_page_without_filling_first_last_name_fields_credintials(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("0534231334")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()
        time.sleep(6)
        sidebar.null_email_assertion()


    def test_sending_message_from_contact_us_page_without_filling_telephone_fields_credintials(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("asdf")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("qwer")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()

    def test_sending_message_from_contact_us_page_with_filling_invalid_email_credintials(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("asdf")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("qwer")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()


    def test_sending_message_from_contact_us_page_with_filling_less_than_10_digit_phone(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("asdf")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("qwer")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("05433421")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()


    def test_sending_message_from_contact_us_page_with_filling_more_than_10_digit_phone(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("asdf")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("qwer")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("05433421123456")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()

    def test_sending_message_from_contact_us_page_with_filling_string_digit_phone(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("asdf")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("qwer")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("adsfgdgdvdb")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()


    def test_sending_message_from_contact_us_page_with_filling_special_character_digit_phone(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("asdf")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("qwer")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("getachew@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("!@#$%^&*()_+")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew")
        time.sleep(1)
        sidebar.click_on_send_button()


    def test_sending_message_from_contact_us_page_by_filling_more_than_100_characters_on_message_field(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("Getachew")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("Gessesse")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("test@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("0534231334")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew cbncvbcvhgsahgfhagsg   ghscgshcgchsc gvchscvshcsva bmsncbhcvjavhcajcvhajcvavchsgcasjchvsjcgvjhcscjjscvja"
                                      "nxbz nxzb nzxb zxzzxcbjsdvdsv jhbdsjhbdskvbdsvjdsbvkdsjvbksdvdskvbjdsvdjskvbdsvs,v dsdsvdsbdsjvkshgcvsjc")
        time.sleep(1)
        sidebar.click_on_send_button()
        sidebar.assertion_valid_message()

    def test_sending_message_from_contact_us_page_by_filling_less_than_100_characters_on_message_field(self):
        sidebar = SideBar(self)
        sidebar.open_trado()
        sidebar.click_option1()
        sidebar.click_option2()
        sidebar.click_save_button()
        time.sleep(3)
        sidebar.click_for_contact_us_link()
        time.sleep(2)
        sidebar.setting_first_name_on_contact_us("Getachew")
        time.sleep(1)
        sidebar.setting_last_name_on_contact_us("Gessesse")
        time.sleep(1)
        sidebar.setting_gmail_contact_us("test@gmail.com")
        time.sleep(1)
        sidebar.setting_phone_contact_us("0534231334")
        time.sleep(1)
        sidebar.setting_message_contact_us("Hi there, this is getachew cbncvbcvhgsac")
        time.sleep(1)
        sidebar.click_on_send_button()
        sidebar.assertion_valid_message()












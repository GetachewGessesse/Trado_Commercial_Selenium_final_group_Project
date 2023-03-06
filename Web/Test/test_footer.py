
from selenium import webdriver
from Web.Page.footer_page import Trado_page
import pytest
import time
import allure

class Test_Trado:

    @allure.description('common_question_button')
    def test_common_question_button(self):
        question = Trado_page(self)
        question.opening_trado()
        question.click_on_save_buttonm()
        question.click_on_common_question()
        question.click_on_back_to_product_page()
        assertion = question.assertion_trado_home_page
        assert assertion == "מבצעים"





    @allure.description('facebook_button_footer')
    def test_facebook_button_footer(self):
        facebook = Trado_page(self)
        facebook.opening_trado()
        facebook.click_on_save_buttonm()
        facebook.click_on_facebook_button_footer()
        facebook.assertion_window_handle()



    @allure.description('test_click_on_shipping_system')
    def test_click_on_shipping_system(self):
        shipping = Trado_page(self)
        shipping.opening_trado()
        shipping.click_on_save_buttonm()
        shipping.click_on_shiping_explantion()
        assertion = shipping.assertion_trado_page
        assert assertion == "אליך עד 72 שעות."


    @allure.description('test_instagram_button_footer')
    def test_instagram_button_footer(self):
        instagram = Trado_page(self)
        instagram.opening_trado()
        instagram.click_on_save_buttonm()
        instagram.click_on_instagram_button_footer()
        instagram.assertion_window_handle_instagram()





    @allure.description('test_max_business_button')
    def test_max_business_button(self):
        max_business = Trado_page(self)
        max_business.opening_trado()
        max_business.click_on_save_buttonm()
        max_business.click_on_max_button_footer()




    @allure.description('test_payment_solution_button')
    def test_payment_solution_button(self):
        payments = Trado_page(self)
        payments.opening_trado()
        payments.click_on_save_buttonm()
        payments.click_on_payment_button_footer()




    @allure.description('test_twitter_button')
    def test_twitter_button(self):
        twitter_footer = Trado_page(self)
        twitter_footer.opening_trado()
        twitter_footer.click_on_save_buttonm()
        twitter_footer.click_on_twitter_button_footer()
        twitter_footer.assertion_window_handle_twitter()





    # Whatsapp_test_Whatsapp_PageWhatsapp_test
    # Whatsapp_test_Whatsapp_test_Whatsapp_test
    # Whatsapp_test_Whatsapp_test_Whatsapp_test

    @allure.description('whatsapp_button')
    def test_whatsapp_button(self):
        whatsapp = Trado_page(self)
        whatsapp.opening_trado()
        whatsapp.click_on_save_buttonm()
        whatsapp.click_on_whatsapp_button()
        whatsapp.click_on_message_field('Hii!!')
        whatsapp.click_on_send_button()

    #
    #
    #
    # # payment_test_payment_test_payment_test_payment_test_payment_test
    # # payment_test_payment_test_payment_test_payment_test_payment_test
    #
    # allure.description('payment_select_product')
    # def test_payment_select_product(self):
    #     select_product = Trado_page(self)
    #     select_product.opening_trado()
    #     select_product.payment_click_on_select_product()
    #     time.sleep(2)
    #     select_product.payment_click_on_add_product()
    #     time.sleep(2)
    #     select_product.payment_click_on_payment_button()
    #     select_product.payment_click_on_complete_purchases()
    #     time.sleep(2)
    #     select_product.payment_click_on_pay_with_credit()
    #     time.sleep(2)
    #     select_product.payment_click_on_credit_card_ID('')
    #     time.sleep(2)
    #     select_product.payment_click_on_userID('')
    #     time.sleep(2)
    #     select_product.payment_click_on_expired_month('')
    #     time.sleep(2)
    #     select_product.payment_click_on_expired_year('')
    #     select_product.payment_click_on_cvv_button('')
    #     time.sleep(2)
    #     select_product.payment_click_on_to_payment_button_ID()
    #     time.sleep(2)
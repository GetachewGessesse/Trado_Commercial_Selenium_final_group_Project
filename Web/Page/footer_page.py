import pytest
from selenium import webdriver
from Web.Locators.footer_locators import Trado_locators
from selenium.webdriver.common.by import By
import time
import allure



class Trado_page(Trado_locators):
    def __init__(self, driver):
        self.driver = driver
        self.url = Trado_locators.trado_url
        self.save = Trado_locators.save_XPATH
        self.common_question = Trado_locators.common_question_link_text
        self.product_page = Trado_locators.product_page_xpath
        self.facebook_button = Trado_locators.facebook_link_text
        self.shipping_system = Trado_locators.how_shiping_link_text
        self.instagram_button = Trado_locators.instagram_link_text
        self.max = Trado_locators.max_business_link_test
        self.payment = Trado_locators.payment_solution_link_text
        self.twitter_button = Trado_locators.twitter_text_link
        self.whatsapp = Trado_locators.whatsapp_XPATH
        self.message_field = Trado_locators.message_field_XPATH
        self.send_message = Trado_locators.send_message_XPATH



    @allure.step
    @allure.description('click_phone')
    def opening_trado(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        # time.sleep(4)
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('click_on_save_buttonm')
    def click_on_save_buttonm(self):
        self.driver.find_element(By.XPATH, self.save).click()
        self.driver.implicitly_wait(10)


    @allure.step
    @allure.description('click_on_common_question')
    def click_on_common_question(self):
        self.driver.find_element(By.LINK_TEXT, self.common_question).click()
        assertion_product = self.driver.find_element(By.XPATH,"//h4[contains(text(),'מכירת סחורה')]").text
        assert assertion_product == "מכירת סחורה"
        self.driver.implicitly_wait(10)




    @allure.step
    @allure.description('click_on_common_question')
    def click_on_back_to_product_page(self):
        self.driver.find_element(By.XPATH, self.product_page).click()
        self.driver.implicitly_wait(10)




    @allure.step
    @allure.description('click_on_common_question')
    def click_on_facebook_button_footer(self):
        self.driver.find_element(By.LINK_TEXT, self.facebook_button).click()
        self.driver.implicitly_wait(10)



    @allure.step
    @allure.description('click_on_common_question')
    def click_on_shiping_explantion(self):
        self.driver.find_element(By.LINK_TEXT, self.shipping_system).click()
        assertion_product = self.driver.find_element(By.XPATH, "//h3[contains(text(),'1. קבלת ההזמנה.')]").text
        assert assertion_product == "1. קבלת ההזמנה."
        self.driver.implicitly_wait(10)




    @allure.step
    @allure.description('click_on_common_question')
    def click_on_instagram_button_footer(self):
        self.driver.find_element(By.LINK_TEXT,self.instagram_button).click()
        self.driver.implicitly_wait(10)




    @allure.step
    @allure.description('click_on_common_question')
    def click_on_max_button_footer(self):
        self.driver.find_element(By.LINK_TEXT,self.max).click()
        self.driver.implicitly_wait(10)




    @allure.step
    @allure.description('click_on_common_question')
    def click_on_payment_button_footer(self):
        self.driver.find_element(By.LINK_TEXT, self.payment).click()
        self.driver.implicitly_wait(10)


    @allure.step
    @allure.description('click_on_common_question')
    def click_on_twitter_button_footer(self):
        self.driver.find_element(By.LINK_TEXT, self.twitter_button).click()
        self.driver.implicitly_wait(10)

    @property
    def assertion_trado_page(self):
        return self.driver.find_element(By.XPATH, "//p[contains(text(),'אליך עד 72 שעות.')]").text

    @property
    def assertion_trado_home_page(self):
        return self.driver.find_element(By.XPATH, "//h1[contains(text(),'מבצעים')]").text


    @allure.step
    @allure.description('click_on_common_question')
    def assertion_window_handle(self):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                assertion_text = self.driver.find_element(By.TAG_NAME, "h2").text
                assert "connect" in assertion_text
                self.driver.switch_to.window(parent_window)
                self.driver.implicitly_wait(10)


    @allure.step
    @allure.description('click_on_common_question')
    def assertion_window_handle_instagram(self):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                assertion_text = self.driver.find_element(By.TAG_NAME, "p").text
                assert "Don't" in assertion_text
                self.driver.switch_to.window(parent_window)
                self.driver.implicitly_wait(10)



    @allure.step
    @allure.description('click_on_common_question')
    def assertion_window_handle_twitter(self):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                assertion_text = self.driver.find_element(By.XPATH, "//span[contains(text(),'חדש בטוויטר?')]").text
                assert "חדש" in assertion_text
                self.driver.switch_to.window(parent_window)
                self.driver.implicitly_wait(10)

    # Whatsapp_Page_Whatsapp_Page_Whatsapp_Page_Whatsapp_Page_
    # Whatsapp_Page_Whatsapp_Page_Whatsapp_Page_Whatsapp_Page_
    # Whatsapp_Page_Whatsapp_Page_Whatsapp_Page_Whatsapp_Page_
    @allure.step
    @allure.description('click_on_common_question')
    def click_on_whatsapp_button(self):
        self.driver.find_element(By.XPATH, self.whatsapp).click()
        assertion_whatsapp = self.driver.find_element(By.XPATH, "//button[contains(text(),'שלח')]").text
        assert assertion_whatsapp == "שלח"
        self.driver.implicitly_wait(10)




    @allure.step
    @allure.description('click_on_common_question')
    def click_on_message_field(self, message_fields):
        self.driver.find_element(By.XPATH, self.message_field).send_keys(message_fields)
        self.driver.implicitly_wait(10)



    @allure.step
    @allure.description('click_on_common_question')
    def click_on_send_button(self):
        self.driver.find_element(By.XPATH, self.send_message).click()
        self.driver.implicitly_wait(10)







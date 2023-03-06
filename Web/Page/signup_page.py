import time

from selenium import webdriver
from Web.Locators.new_signup_locators import SignupLocators
from selenium.webdriver.common.by import By
import allure


class SignUp():

    def __init__(self, driver):
        self.driver = driver

        self.website = SignupLocators.website
        self.connection_className = SignupLocators.connection_className
        self.option1_xpath = SignupLocators.option1_xpath
        self.option2_xpath = SignupLocators.option2_xpath
        self.save = SignupLocators.save
        self.signup_link_xpath = SignupLocators.signup_link_xpath
        self.login_facebook_button_className = SignupLocators.login_facebook_button_className
        self.login_google_button_className = SignupLocators.login_google_button_className
        self.login_twitter_button_className = SignupLocators.login_twitter_button_className
        self.login_phone_input_xpath =  SignupLocators.login_phone_input_xpath
        self.user_name_xpath = SignupLocators.user_name_xpath
        self.password_xpath = SignupLocators.password_xpath
        self.login_button_class_name = SignupLocators.login_button_class_name
        self.privacy_policy_checkbox_xpath= SignupLocators.privacy_policy_checkbox_xpath
        self.business_number_field_xpath = SignupLocators.business_number_field_xpath
        self.privacy_poicy_error_message_xpath = SignupLocators.privacy_poicy_error_message_xpath



    @allure.step
    @allure.description('Navigate to demoblaz website')
    def open_trado(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.maximize_window()

    def click_option1(self):
        self.driver.find_element(By.XPATH, self.option1_xpath).click()

    def click_option2(self):
        self.driver.find_element(By.XPATH, self.option2_xpath).click()

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save).click()

    def click_on_connect_link(self):
        self.driver.find_element(By.CLASS_NAME, self.connection_className).click()

    def click_on_twitter_link(self):
        self.driver.find_element(By.CLASS_NAME, self.login_twitter_button_className).click()

    def click_on_signup_link(self):
        self.driver.find_element(By.XPATH, self.signup_link_xpath).click()

    def click_on_facebook_link(self):
        self.driver.find_element(By.CLASS_NAME, self.login_facebook_button_className).click()

    def click_on_google_link(self):
        self.driver.find_element(By.CLASS_NAME, self.login_google_button_className).click()


    def click_privacy_policy(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_checkbox_xpath).click()

    def click_on_signup_button(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button_class_name).click()

    def setting_phone_number(self, phone):
        self.driver.find_element(By.XPATH, self.login_phone_input_xpath).send_keys(phone)

    def setting_buisness_number(self, buisness_number):
        self.driver.find_element(By.XPATH, self.business_number_field_xpath).send_keys(buisness_number)

    def window_handle(self):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                twitter_url = self.driver.current_url
                assert "twitter "in twitter_url

    def window_handle_facebook(self, username, password):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                self.driver.find_element(By.ID, "email").send_keys(username)
                self.driver.find_element(By.ID, "pass").send_keys(password)
                time.sleep(3)
                self.driver.find_element(By.NAME, "login").click()
                facebook_title = self.driver.title
                print(facebook_title)
                assert "home" in facebook_title


    def window_handle_facebook_with_error_message(self, username, password):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for handle in all_windows:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                self.driver.find_element(By.ID, "email").send_keys(username)
                self.driver.find_element(By.ID, "pass").send_keys(password)
                time.sleep(3)
                self.driver.find_element(By.NAME, "login").click()


    @allure.step
    @allure.description('Clear and send keys to username field')
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.user_name_xpath).clear()
        self.driver.find_element(By.ID, self.user_name_xpath ).send_keys(username)

    @allure.step
    @allure.description('Clear and send keys to password field')
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_xpath).clear()
        self.driver.find_element(By.ID, self.password_xpath ).send_keys(password)


    @property
    def error_message_getter(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'מס׳ טלפון לא תקין')]").text

    @property
    def error_message_getter2(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text

    @property
    def error_message_privacy_policy(self):
        return self.driver.find_element(By.XPATH, self.privacy_poicy_error_message_xpath).text


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.new_login_locators import LoginLocators
import allure


class Login():

    def __init__(self, driver):
        self.driver = driver

        self.website = LoginLocators.website
        self.connection_className = LoginLocators.connection_className
        self.option1_xpath = LoginLocators.option1_xpath
        self.option2_xpath = LoginLocators.option2_xpath
        self.save = LoginLocators.save
        self.login_facebook_button_className = LoginLocators.login_facebook_button_className
        self.login_google_button_className = LoginLocators.login_google_button_className
        self.login_twitter_button_className = LoginLocators.login_twitter_button_className
        self.login_phone_input_xpath = LoginLocators.login_phone_input_xpath
        self.user_name_xpath = LoginLocators.user_name_xpath
        self.password_xpath =  LoginLocators.password_xpath
        self.login_button_class_name = LoginLocators.login_button_class_name
        self.checkbox_className = LoginLocators.checkbox_className

    @allure.step
    @allure.description('Navigate to demoblaz website')
    def open_demoblaz(self):
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

    def click_on_facebook_link(self):
        self.driver.find_element(By.CLASS_NAME, self.login_facebook_button_className).click()

    def click_on_google_link(self):
        self.driver.find_element(By.CLASS_NAME, self.login_google_button_className).click()


    def click_checkbox(self):
        self.driver.find_element(By.CLASS_NAME, self.checkbox_className).click()

    def click_on_login_button(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button_class_name).click()

    def setting_phone_number(self, phone):
        self.driver.find_element(By.XPATH, self.login_phone_input_xpath).send_keys(phone)

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


    def inserting_login_using_mongodb_cloud(self):
        from pymongo import MongoClient
        cluster = "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority"
        db_client = MongoClient(cluster)
        # print(db_client.list_database_names())
        # server_info = db_client.server_info()
        # print(server_info)
        db = db_client['trado_qa']
        # collections = db.list_collection_names()
        # print(collections)
        collection = db['users']

        results = collection.find({"email": 'israel.mangisto@gmail.com'})

        for resuit in results:
            login_code = str((resuit['loginCode']))
            print(login_code)
            print(login_code[0])
            print(login_code[1])
            print(login_code[2])
            print(login_code[3])
            print(login_code[4])
    # def click_on_login_button(self):
    #     self.driver.find_element(By.CLASS_NAME, self.login_button_class_name).click()

    # @allure.step
    # @allure.description('Click on login link text')
    # def click_on_login_link(self):
    #     self.driver.find_element(By.LINK_TEXT, self.login_link_locator_linkText).click()
    #
    #
    # @allure.step
    # @allure.description('Clear and send keys to username field')
    # def setUsername(self, username):
    #     self.driver.find_element(By.ID, self.login_username_field_locator_id).clear()
    #     self.driver.find_element(By.ID, self.login_username_field_locator_id ).send_keys(username)
    #
    # @allure.step
    # @allure.description('Clear and send keys to password field')
    # def setPassword(self, password):
    #     self.driver.find_element(By.ID, self.login_password_field_locator_id).clear()
    #     self.driver.find_element(By.ID, self.login_password_field_locator_id ).send_keys(password)
    #
    # @allure.step
    # @allure.description('Click on login button')
    # def click_on_login_button(self):
    #     self.driver.find_element(By.XPATH, self.login_button_locator_xpath).click()
    #
    # @allure.step
    # @allure.description('Click on close button')
    # def click_on_close_button(self):
    #     self.driver.find_element(By.XPATH, self.login_close_button_locator_xpath).click()
    #
    # @property
    # @allure.step
    # @allure.description('Verify the welcome text displayed after login')
    # def welcome_text_getter(self):
    #     return self.driver.find_element(By.ID, self.welcome_txt_locator_id).text
    #
    # @allure.step
    # @allure.description('Click on close button')
    # def click_logout_link(self):
    #     self.driver.find_element(By.ID, self.logout_link_locator_id).click()
    #
    #
    # @allure.step
    # @allure.description('Click ok/ accept popup alert message')
    # def alert_popup_accepter(self):
    #     self.driver.switch_to.alert.accept()
    #
    # @property
    # @allure.step
    # @allure.description('Extracting message from popup alert window')
    # def alert_popup_text(self):
    #     return self.driver.switch_to.alert.text
    #
    #
    # @property
    # @allure.step
    # @allure.description('Verify the login text displayed after logout')
    # def login_text_getter(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.login_link_locator_linkText ).text
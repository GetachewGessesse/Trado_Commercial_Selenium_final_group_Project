import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.new_sidebar_locators import SidebarLocators
import allure


class SideBar():

    def __init__(self, driver):
        self.driver = driver

        self.website = SidebarLocators.website
        self.connection_className =  SidebarLocators.connection_className
        self.option1_xpath = SidebarLocators.option1_xpath
        self.option2_xpath = SidebarLocators.option2_xpath
        self.save = SidebarLocators.save
        self.for_uses_side_bar_xpath = SidebarLocators.for_uses_side_bar_xpath
        self.for_common_questions_linktext = SidebarLocators.for_common_questions_linktext
        self.for_contact_us_linktext = SidebarLocators.for_contact_us_linktext
        self.for_how_delivery_works_xpath = SidebarLocators.for_how_delivery_works_xpath
        self.first_name_contact_xpath = SidebarLocators.first_name_contact_xpath
        self.last_name_contact_xpath = SidebarLocators.last_name_contact_xpath
        self.gmail_contact_path = SidebarLocators.gmail_contact_path
        self.phone_contact_xpath = SidebarLocators.phone_contact_xpath
        self.message_field_xpath = SidebarLocators.message_field_xpath
        self.send_button_xpath = SidebarLocators.send_button_xpath

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

    def click_on_for_uses_side_bar_link(self):
        self.driver.find_element(By.XPATH, self.for_uses_side_bar_xpath).click()

    def click_for_common_questionslink(self):
        self.driver.find_element(By.LINK_TEXT, self.for_common_questions_linktext).click()
        assertion_text = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h4[1]").text
        assert "יש לכם שאלות" in assertion_text
        assert "הגעתם למקום" in assertion_text

    def click_for_contact_us_link(self):
        self.driver.find_element(By.LINK_TEXT, self.for_contact_us_linktext).click()
        assertion_text = self.driver.find_element(By.TAG_NAME, "h4").text
        assert "נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה." == assertion_text

    def click_for_how_delivery_workslink(self):
        self.driver.find_element(By.XPATH, self.for_how_delivery_works_xpath).click()
        assertion_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'שיטת השילוח שלנו נורא פשוטה.')]").text
        assert "שיטת השילוח שלנו נורא פשוטה" in assertion_text

    def setting_first_name_on_contact_us(self, firstname):
        self.driver.find_element(By.XPATH, self.first_name_contact_xpath).send_keys(firstname)

    def setting_last_name_on_contact_us(self, lastname):
        self.driver.find_element(By.XPATH, self.last_name_contact_xpath).send_keys(lastname)

    def setting_gmail_contact_us(self, gmail):
        self.driver.find_element(By.XPATH, self.gmail_contact_path).send_keys(gmail)

    def setting_phone_contact_us(self, phone):
        self.driver.find_element(By.XPATH, self.phone_contact_xpath).send_keys(phone)

    def setting_message_contact_us(self, message):
        self.driver.find_element(By.XPATH, self.message_field_xpath).send_keys(message)

    def click_on_send_button(self):
        self.driver.find_element(By.XPATH, self.send_button_xpath).click()
        time.sleep(5)

    def assertion_valid_message(self):
        asserion_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'הפרטים נקלטו בהצלחה')]").text
        assert "הפרטים נקלטו בהצלחה" in asserion_message

    def null_message_assertion(self):
        assertion = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]").text
        assert "נא למלא שדה זה" == assertion

    def null_email_assertion(self):
        assertion = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]").text
        assert "נא למלא שדה זה" in assertion

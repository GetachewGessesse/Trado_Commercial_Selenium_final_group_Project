import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.snack_locatores import Snack_locatores
import allure
from selenium.webdriver.support.select import Select


class Snack_page():

    def __init__(self, driver):
        self.driver = driver
        self.website = Snack_locatores.website
        self.snack_xpath = Snack_locatores.snack_xpath
        self.sort_xpath = Snack_locatores.sort_xpath
        self.view_landscape_xpath = Snack_locatores.view_landscape_xpath
        self.view_grid_xpath = Snack_locatores.view_grid_xpath
        self.pro_prigat_xpath = Snack_locatores.pro_prigat_xpath
        self.pro_prigat_plus_xpath = Snack_locatores.pro_prigat_plus_xpath
        self.pro_prigat_minus_xpath = Snack_locatores.pro_prigat_minus_xpath
        self.option1_xpath = Snack_locatores.option1_xpath
        self.option2_xpath = Snack_locatores.option2_xpath
        self.save = Snack_locatores.save
        self.website = Snack_locatores.website
        self.connection_className = Snack_locatores.connection_className
        self.option1_xpath = Snack_locatores.option1_xpath
        self.option2_xpath = Snack_locatores.option2_xpath
        self.save = Snack_locatores.save
        self.for_uses_side_bar_xpath = Snack_locatores.for_uses_side_bar_xpath
        self.for_common_questions_linktext = Snack_locatores.for_common_questions_linktext
        self.for_contact_us_linktext = Snack_locatores.for_contact_us_linktext
        self.for_how_delivery_works_xpath = Snack_locatores.for_how_delivery_works_xpath
        self.first_name_contact_xpath = Snack_locatores.first_name_contact_xpath
        self.last_name_contact_xpath = Snack_locatores.last_name_contact_xpath
        self.gmail_contact_path = Snack_locatores.gmail_contact_path
        self.phone_contact_xpath = Snack_locatores.phone_contact_xpath
        self.message_field_xpath = Snack_locatores.message_field_xpath
        self.send_button_xpath = Snack_locatores.send_button_xpath

    @allure.step
    @allure.description('Navigate to demoblaz website')
    def open_trado(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.maximize_window()

    @allure.step
    @allure.description('click option1')
    def click_option1(self):
        self.driver.find_element(By.XPATH, self.option1_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('click option2')
    def click_option2(self):
        self.driver.find_element(By.XPATH, self.option2_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('save_button')
    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('navigate snack Page')
    def click_on_snack_page(self):
        self.driver.find_element(By.XPATH, self.snack_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('landscape view option')
    def click_on_landscape_view(self):
        self.driver.find_element(By.XPATH, self.view_landscape_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('grid view option')
    def click_on_grid_view(self):
        self.driver.find_element(By.XPATH, self.view_grid_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('product prigat')
    def click_on_product_prigat(self):
        self.driver.find_element(By.XPATH, self.pro_prigat_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('adding prigat product to cart')
    def click_on_product_prigat_plus(self):
        self.driver.find_element(By.XPATH, self.pro_prigat_plus_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('removing prigat product from cart')
    def click_on_product_prigat_minus(self):
        self.driver.find_element(By.XPATH, self.pro_prigat_minus_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('sort by popularity')
    def sort_by_popularity(self):
        sort = Select(self.driver.find_element(By.XPATH, self.sort_xpath))
        sort.select_by_value("popularity")
        self.driver.implicitly_wait(10)


    @allure.step
    @allure.description('sort by highest price')
    def sort_by_highest_price(self):
        sort = Select(self.driver.find_element(By.XPATH, self.sort_xpath))
        sort.select_by_value('{"price":1}')
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('sort of lowest price')
    def sort_by_lowest_price(self):
        sort = Select(self.driver.find_element(By.XPATH, self.sort_xpath))
        sort.select_by_value('{"price":-1}')
        self.driver.implicitly_wait(10)





    @property
    @allure.step
    @allure.description('verify snack Page is opened')
    def snack_assertion(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text

    @property
    @allure.step
    @allure.description('verify if the lower price product is displayed firstly')
    def lower_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'1.00₪')]").text

    @allure.step
    @allure.description('verify if the lower price product is displayed second')
    def second_lowest_price_assertion(self):
        assertion_2 = self.driver.find_element(By.XPATH, "//span[contains(text(),'10000.00₪')]").text
        assert assertion_2 == '99.46₪'

    @property
    @allure.step
    @allure.description('verify if the highest price product is displayed firstly')
    def highest_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'10000.00₪')]").text

    @property
    @allure.step
    @allure.description('verify if the popularity price product is displayed firstly')
    def popularity_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'goats')]").text

    @property
    @allure.step
    @allure.description('verify if the product is added ')
    def add_product_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'₪117,000.00')]").text

    @property
    @allure.step
    @allure.description('verify if the product is added ')
    def minus_product_assertion(self):
        return self.driver.find_element(By.XPATH, "//h5[contains(text(),'העגלה שלך ריקה')]").text

    @allure.step
    @allure.description('Navigate to demoblaz website')
    def open_trado(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.maximize_window()

    # def click_option1(self):
    #     self.driver.find_element(By.XPATH, self.option1_xpath).click()
    #
    # def click_option2(self):
    #     self.driver.find_element(By.XPATH, self.option2_xpath).click()
    #
    # def click_save_button(self):
    #     self.driver.find_element(By.XPATH, self.save).click()

    def click_on_for_uses_side_bar_link(self):
        self.driver.find_element(By.XPATH, self.for_uses_side_bar_xpath).click()
        self.driver.implicitly_wait(10)

    def click_for_common_questionslink(self):
        self.driver.find_element(By.LINK_TEXT, self.for_common_questions_linktext).click()
        assertion_text = self.driver.find_element(By.XPATH,
                                                  "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h4[1]").text
        assert "יש לכם שאלות" in assertion_text
        assert "הגעתם למקום" in assertion_text
        self.driver.implicitly_wait(10)

    def click_for_contact_us_link(self):
        self.driver.find_element(By.LINK_TEXT, self.for_contact_us_linktext).click()
        assertion_text = self.driver.find_element(By.TAG_NAME, "h4").text
        assert "נשמח לעמוד לרשותך בכל שאלה, בקשה או הערה." == assertion_text
        self.driver.implicitly_wait(10)

    def click_for_how_delivery_workslink(self):
        self.driver.find_element(By.XPATH, self.for_how_delivery_works_xpath).click()
        assertion_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'שיטת השילוח שלנו נורא פשוטה.')]").text
        assert "שיטת השילוח שלנו נורא פשוטה" in assertion_text
        self.driver.implicitly_wait(10)

    def setting_first_name_on_contact_us(self, firstname):
        self.driver.find_element(By.XPATH, self.first_name_contact_xpath).send_keys(firstname)
        self.driver.implicitly_wait(10)

    def setting_last_name_on_contact_us(self, lastname):
        self.driver.find_element(By.XPATH, self.last_name_contact_xpath).send_keys(lastname)
        self.driver.implicitly_wait(10)

    def setting_gmail_contact_us(self, gmail):
        self.driver.find_element(By.XPATH, self.gmail_contact_path).send_keys(gmail)
        self.driver.implicitly_wait(10)

    def setting_phone_contact_us(self, phone):
        self.driver.find_element(By.XPATH, self.phone_contact_xpath).send_keys(phone)
        self.driver.implicitly_wait(10)

    def setting_message_contact_us(self, message):
        self.driver.find_element(By.XPATH, self.message_field_xpath).send_keys(message)
        self.driver.implicitly_wait(10)

    def click_on_send_button(self):
        self.driver.find_element(By.XPATH, self.send_button_xpath).click()
        self.driver.implicitly_wait(10)

    def assertion_valid_message(self):
        asserion_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'הפרטים נקלטו בהצלחה')]").text
        assert "הפרטים נקלטו בהצלחה" in asserion_message

    def null_message_assertion(self):
        assertion = self.driver.find_element(By.XPATH,
                                             "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]").text
        assert "נא למלא שדה זה" == assertion

    def null_email_assertion(self):
        assertion = self.driver.find_element(By.XPATH,
                                             "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]").text
        assert "נא למלא שדה זה" in assertion

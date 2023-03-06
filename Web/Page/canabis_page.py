import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.select import Select
from Web.Locators.canabis_locators import Canabis_locatores


class Canabis_page():

    def __init__(self, driver):
        self.driver = driver
        self.website = Canabis_locatores.website
        self.canabis_xpath = Canabis_locatores.canabis_xpath
        self.sort_xpath = Canabis_locatores.sort_xpath
        self.view_landscape_xpath = Canabis_locatores.view_landscape_xpath
        self.view_grid_xpath = Canabis_locatores.view_grid_xpath
        self.pro_Hashplant_xpath = Canabis_locatores.pro_Hashplant_xpath
        self.pro_Hashplant_plus_xpath = Canabis_locatores.pro_Hashplant_plus_xpath
        self.pro_Hashplant_minus_xpath = Canabis_locatores.pro_Hashplant_minus_xpath
        self.option1_xpath = Canabis_locatores.option1_xpath
        self.option2_xpath = Canabis_locatores.option2_xpath
        self.save = Canabis_locatores.save
        self.website = Canabis_locatores.website
        self.connection_className = Canabis_locatores.connection_className
        self.option1_xpath = Canabis_locatores.option1_xpath
        self.option2_xpath = Canabis_locatores.option2_xpath
        self.save = Canabis_locatores.save
        self.for_uses_side_bar_xpath = Canabis_locatores.for_uses_side_bar_xpath
        self.for_common_questions_linktext = Canabis_locatores.for_common_questions_linktext
        self.for_contact_us_linktext = Canabis_locatores.for_contact_us_linktext
        self.for_how_delivery_works_xpath = Canabis_locatores.for_how_delivery_works_xpath
        self.first_name_contact_xpath = Canabis_locatores.first_name_contact_xpath
        self.last_name_contact_xpath = Canabis_locatores.last_name_contact_xpath
        self.gmail_contact_path = Canabis_locatores.gmail_contact_path
        self.phone_contact_xpath = Canabis_locatores.phone_contact_xpath
        self.message_field_xpath = Canabis_locatores.message_field_xpath
        self.send_button_xpath = Canabis_locatores.send_button_xpath

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
    @allure.description('navigate canabis Page')
    def click_on_canabis_page(self):
        self.driver.find_element(By.XPATH, self.canabis_xpath).click()
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
    @allure.description('product Hashplant')
    def click_on_product_Hashplant(self):
        self.driver.find_element(By.XPATH, self.pro_Hashplant_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('adding Hashplant product to cart')
    def click_on_product_Hashplant_plus(self):
        self.driver.find_element(By.XPATH, self.pro_Hashplant_plus_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('removing Hashplant product from cart')
    def click_on_product_Hashplant_minus(self):
        self.driver.find_element(By.XPATH, self.pro_Hashplant_minus_xpath).click()
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
    def canabis_assertion(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text

    @property
    @allure.step
    @allure.description('verify if the lower price product is displayed firstly')
    def lower_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'229.00₪')]").text


    @property
    @allure.step
    @allure.description('verify if the highest price product is displayed firstly')
    def highest_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'2290.00₪')]").text

    @property
    @allure.step
    @allure.description('verify if the popularity price product is displayed firstly')
    def popularity_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'גורילה גלו')]").text

    @property
    @allure.step
    @allure.description('verify if the product is added ')
    def add_product_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'₪33.81')]").text

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


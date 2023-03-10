import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.sales_locatores import Sales_locatores
import allure
from selenium.webdriver.support.select import Select


class Sales_page():

    def __init__(self, driver):
        self.driver = driver
        self.website = Sales_locatores.website
        self.sales_xpath = Sales_locatores.sales_xpath
        self.sort_xpath = Sales_locatores.sort_xpath
        self.view_landscape_xpath = Sales_locatores.view_landscape_xpath
        self.view_grid_xpath = Sales_locatores.view_grid_xpath
        self.pro_ogkush_xpath = Sales_locatores.pro_ogkush_xpath
        self.pro_ogkush_plus_xpath = Sales_locatores.pro_ogkush_plus_xpath
        self.pro_ogkush_minus_xpath = Sales_locatores. pro_ogkush_minus_xpath
        self.option1_xpath = Sales_locatores.option1_xpath
        self.option2_xpath = Sales_locatores.option2_xpath
        self.save = Sales_locatores.save
        self.next_pic_xpath = Sales_locatores.next_pic_xpath
        self.preview_pic_xpath = Sales_locatores.preview_pic_xpath
        self.website = Sales_locatores.website
        self.connection_className = Sales_locatores.connection_className
        self.option1_xpath = Sales_locatores.option1_xpath
        self.option2_xpath = Sales_locatores.option2_xpath
        self.save = Sales_locatores.save
        self.for_uses_side_bar_xpath = Sales_locatores.for_uses_side_bar_xpath
        self.for_common_questions_linktext = Sales_locatores.for_common_questions_linktext
        self.for_contact_us_linktext = Sales_locatores.for_contact_us_linktext
        self.for_how_delivery_works_xpath = Sales_locatores.for_how_delivery_works_xpath
        self.first_name_contact_xpath = Sales_locatores.first_name_contact_xpath
        self.last_name_contact_xpath = Sales_locatores.last_name_contact_xpath
        self.gmail_contact_path = Sales_locatores.gmail_contact_path
        self.phone_contact_xpath = Sales_locatores.phone_contact_xpath
        self.message_field_xpath = Sales_locatores.message_field_xpath
        self.send_button_xpath = Sales_locatores.send_button_xpath

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
    @allure.description('navigate sales Page')
    def click_on_sale_page(self):
        self.driver.find_element(By.XPATH, self.sales_xpath).click()
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
    @allure.description('next slide picture')
    def click_on_next_picture(self):
        self.driver.find_element(By.XPATH, self.next_pic_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('preview slide picture')
    def click_on_preview_picture(self):
        self.driver.find_element(By.XPATH, self.preview_pic_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('product ogkush')
    def click_on_product_ogkush(self):
        self.driver.find_element(By.XPATH, self.pro_ogkush_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('adding ogkush product to cart')
    def click_on_product_ogkush_plus(self):
        self.driver.find_element(By.XPATH, self.pro_ogkush_plus_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('removing ogkush product from cart')
    def click_on_product_ogkush_minus(self):
        self.driver.find_element(By.XPATH, self.pro_ogkush_minus_xpath).click()
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
    @allure.description('verify drink Page is opened')
    def sales_assertion(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text


    @property
    @allure.step
    @allure.description('verify if the lower price product is displayed firstly')
    def lower_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'1.00???')]").text


    @allure.step
    @allure.description('verify if the lower price product is displayed second')
    def second_lowest_price_assertion(self):
        assertion_2 = self.driver.find_element(By.XPATH, "//span[contains(text(),'1000.00???')]").text
        assert assertion_2 == '99.46???'

    @property
    @allure.step
    @allure.description('verify if the highest price product is displayed firstly')
    def highest_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'555.00???')]").text

    @allure.step
    @allure.description('verify if the highest price product is displayed second')
    def second_highest_price_assertion(self):
        assertion_2 = self.driver.find_element(By.XPATH, "//span[contains(text(),'1000.00???')]").text
        assert assertion_2 == '99.00???'



    @property
    @allure.step
    @allure.description('verify if the popularity price product is displayed firstly')
    def popularity_price_assertion(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'???????????? ??????')]").text

    @property
    @allure.step
    @allure.description('verify if the product is added ')
    def add_product_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'???27.96')]").text

    @property
    @allure.step
    @allure.description('verify if the product is added ')
    def minus_product_assertion(self):
        return self.driver.find_element(By.XPATH, "//h5[contains(text(),'?????????? ?????? ????????')]").text

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
        assert "???? ?????? ??????????" in assertion_text
        assert "?????????? ??????????" in assertion_text
        self.driver.implicitly_wait(10)

    def click_for_contact_us_link(self):
        self.driver.find_element(By.LINK_TEXT, self.for_contact_us_linktext).click()
        assertion_text = self.driver.find_element(By.TAG_NAME, "h4").text
        assert "???????? ?????????? ???????????? ?????? ????????, ???????? ???? ????????." == assertion_text
        self.driver.implicitly_wait(10)

    def click_for_how_delivery_workslink(self):
        self.driver.find_element(By.XPATH, self.for_how_delivery_works_xpath).click()
        assertion_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'???????? ???????????? ???????? ???????? ??????????.')]").text
        assert "???????? ???????????? ???????? ???????? ??????????" in assertion_text
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
        asserion_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'???????????? ?????????? ????????????')]").text
        assert "???????????? ?????????? ????????????" in asserion_message

    def null_message_assertion(self):
        assertion = self.driver.find_element(By.XPATH,
                                             "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]").text
        assert "???? ???????? ?????? ????" == assertion

    def null_email_assertion(self):
        assertion = self.driver.find_element(By.XPATH,
                                             "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]").text
        assert "???? ???????? ?????? ????" in assertion



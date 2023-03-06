import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locators.search_locaters import SearchLocators
import allure


class Search():

    def __init__(self, driver):
        self.driver = driver
        self.website = SearchLocators.url
        self.option1_xpath = SearchLocators.option1_XPATH
        self.option2_xpath = SearchLocators.option2_XPATH
        self.save = SearchLocators.save_XPATH
        self.search_xpath = SearchLocators.search_box_xpath
        self.goat_milk = SearchLocators.goats_milk_xpath
        self.no_product = SearchLocators.no_product_xpath


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

    def clear_item_from_search_field(self):
        self.driver.find_element(By.XPATH, self.search_xpath).clear()
        time.sleep(4)

    def send_keys_on_search_box(self, item):
        self.driver.find_element(By.XPATH, self.search_xpath).send_keys(item)


    def send_keys_on_search_box_second_time(self, item2):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search_xpath).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.search_xpath).send_keys(item2)
        time.sleep(3)

    @property
    def assertion_for_existing_product(self):
        return self.driver.find_element(By.XPATH, self.goat_milk).text

    @property
    def assertion_for_no_product(self):
        return self.driver.find_element(By.XPATH, self.no_product).text


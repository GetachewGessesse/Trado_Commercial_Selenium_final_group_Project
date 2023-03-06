import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.select import Select
from Web.Locators.cart_locators import CART


class Cart_page():

    def __init__(self, driver):
        self.driver = driver
        self.website = CART.website
        self.cart_click_on_sample_product1 = CART.cart_click_on_sample_product1
        self.cart_click_on_plus_radio_button_to_add_to_cart= CART.cart_click_on_plus_radio_button_to_add_to_cart
        self.cart_check_the_product_if_added_to_cart = CART.cart_check_the_product_if_added_to_cart
        self.cart_click_on_minus_radio_button_to_add_to_cart = CART.cart_click_on_minus_radio_button_to_add_to_cart
        self.cart_click_on_sample_product2 = CART. cart_click_on_sample_product2
        self.cart_click_on_sum_total = CART.cart_click_on_sum_total
        self.cart_delete_product = CART.cart_delete_product
        self.cart_checkout_button = CART.cart_checkout_button
        self.option1_xpath = CART.option1_xpath
        self.option2_xpath = CART.option2_xpath
        self.save = CART.save

    @allure.step
    @allure.description('Navigate to qa.trado.co.il website')
    def open_website(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.maximize_window()

    def click_on_product(self):
        self.driver.find_element(By.XPATH, self.cart_click_on_sample_product1).click()
        self.driver.implicitly_wait(10)

    def click_on_radio_plus_button(self):
        self.driver.find_element(By.XPATH, self.cart_click_on_plus_radio_button_to_add_to_cart).click()
        self.driver.implicitly_wait(10)

    def click_on_radio_minus_button(self):
        self.driver.find_element(By.XPATH, self.cart_click_on_minus_radio_button_to_add_to_cart).click()
        self.driver.implicitly_wait(10)

    def click_on_sample_product_button(self):
        self.driver.find_element(By.XPATH, self.cart_click_on_sample_product2).click()
        self.driver.implicitly_wait(10)

    def click_on_sumtotal_button(self):
        self.driver.find_element(By.XPATH, self.cart_click_on_sum_total).click()
        self.driver.implicitly_wait(10)

    def click_delete_button(self):
        self.driver.find_element(By.XPATH, self.cart_delete_product).click()
        self.driver.implicitly_wait(10)

    def click_checkout_buttons(self):
        self.driver.find_element(By.XPATH, self.cart_checkout_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('click option1')
    def click_option1(self):
        self.driver.find_element(By.XPATH, self.option1_xpath).click()
        time.sleep(3)

    @allure.step
    @allure.description('click option2')
    def click_option2(self):
        self.driver.find_element(By.XPATH, self.option2_xpath).click()
        time.sleep(3)

    @allure.step
    @allure.description('save_button')
    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save).click()
        time.sleep(3)



    @property
    @allure.step
    @allure.description('Verify all the user interface in the page')
    def carts_ball_go(self):
        return self.driver.find_element(By.XPATH, "//h1[contains(text(),'מבצעים')]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_plus(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'בדיקה חדשה 1')]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_plus_add(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_same(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'אקדיה')]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_product(self):
        return self.driver.find_element(By.XPATH, "//h1[contains(text(),'אקדיה')]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_delete(self):
        return self.driver.find_element(By.XPATH, "//h5[contains(text(),'העגלה שלך ריקה')]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_sequence(self):
        return self.driver.find_element(By.XPATH, "//h2[contains(text(),'ברוכים השבים! מתרגשים לראות אתכם כאן')]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_excat_amount(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball_multiple(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'₪33.81')]").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text

    @property
    @allure.step
    @allure.description('')
    def carts_ball(self):
        return self.driver.find_element(By.XPATH, "").text






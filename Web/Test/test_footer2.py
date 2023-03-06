import time

import pytest
from selenium.webdriver.common.by import By
from Web.Base.base_test import Base_test
from Web.Page.page_footer2 import footerLink
import allure


class Test(Base_test):

    @allure.description('Chech who we are link')
    @pytest.mark.sanity
    def test_footer_link_click(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.footerLink()

    @allure.description('Chech who we are link')
    @pytest.mark.sanity
    def test_who_we_link(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()

    @allure.description('scroll page')
    @pytest.mark.sanity
    def test_scrolling_who_we_link(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()
        time.sleep(2)
        footer_page.scroll_page_up()
        time.sleep(2)

    @allure.description('MORE DETAILS')
    @pytest.mark.sanity
    def test_More_details_link(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()
        footer_page.More_details_link()
        # assertion_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'פרטים נוספים')]").text
        # assert assertion_button == "פרטים נוספים"



    @allure.description('Technological_delivery')
    @pytest.mark.sanity
    def test_Technological_delivery(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()
        #login_page.More_details_link()
        assertion_display_text = self.driver.find_element(By.XPATH, "h4").text
        assert assertion_display_text == 'מערך משלוחים טכנולוגי'
        time.sleep(2)

    @allure.description('advance payment')
    @pytest.mark.sanity
    def test_advanced_payment(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()
        #login_page.More_details_link()
        assertion_advance_text = self.driver.find_element(By.XPATH, "//h4[contains(text(),'אפשרויות תשלום מתקדמות')]").text
        assert assertion_advance_text == 'אפשרויות תשלום מתקדמות'

    @allure.description('buying selling')
    @pytest.mark.sanity
    def test_buyning_selling(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()
        # assertion_buying_text = self.driver.find_element(By.XPATH, "//h4[contains(text(),'רכישה ומכירה אנונימית')]").text
        # assert assertion_buying_text == 'רכישה ומכירה אנונימית'

    @allure.description('New order linck')
    @pytest.mark.sanity
    def test_Order_New(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()
        footer_page.New_Order_Link()

        assertion_buying_text = self.driver.find_element(By.XPATH, "//a[contains(text(),'הזמנה חדשה')]").text
        assert assertion_buying_text == 'הזמנה חדשה'

    @allure.description('To trading')
    @pytest.mark.sanity
    def test_to_Trading_linck(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.who_we_are_link()
        time.sleep(2)
        footer_page.trading_link()
        time.sleep(2)

    @allure.description('etrado')
    @pytest.mark.sanity
    def test_Eterado_link(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.E_torado_link()

    @allure.description('business interface')
    @pytest.mark.sanity
    def test_busines_interface_link(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()

    @allure.description('business interface insert all correct data')
    @pytest.mark.sanity
    def test_coctail_select_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('alex')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_cocktail()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')

    @allure.description('business interface for restaurant correct data')
    @pytest.mark.sanity
    def test_restaurant_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('alex ')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_resturant()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')

    @allure.description('business interface with out first name')
    @pytest.mark.sanity
    def test_empty_fnameof_resturat_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')

        footer_page.categories_field()
        footer_page.categories_by_resturant()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('234')
        footer_page.street_field('zehal nign')
        footer_page.city_field('sefad')

        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('business interface With out firs name and last name for resturant')
    @pytest.mark.sanity
    def test_empty_fname_and_lname_resturannt_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('')
        footer_page.Last_name_field('')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_resturant()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')
        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('business interface with out EM AND HP')
    @pytest.mark.sanity
    def test_empty_HP_EM_resturant_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('alex')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_resturant()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')
        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('business interface with out email')
    @pytest.mark.sanity
    def test_empty_email_resturant_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('alex')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_resturant()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')
        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('business interface with out EM number')
    @pytest.mark.sanity
    def test_empty_phone_resturant_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('alex')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_resturant()
        footer_page.phon_number_field('')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')
        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('business interface with out address')
    @pytest.mark.sanity
    def test_empty_city_street_resturant_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('alex')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_resturant()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('')
        footer_page.city_field('')
        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('business interface without fname and last name')
    @pytest.mark.sanity
    def test_emity_Fname_and_Lnmae_coctail_select_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('')
        footer_page.Last_name_field('')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_cocktail()
        footer_page.phon_number_field('0533560645')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')
        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('business interface with phopne number no number')
    @pytest.mark.sanity
    def test_incorrect_phonnumber_coctail_select_field(self):
        driver = self.driver
        footer_page = footerLink(driver)
        footer_page.open()
        footer_page.Busines_interface_link()
        time.sleep(3)
        footer_page.First_name_field('alex')
        footer_page.Last_name_field('yalew')
        footer_page.HP_EM_field('12')
        footer_page.Business_name_field('quality assurance')
        footer_page.categories_field()
        footer_page.categories_by_cocktail()
        footer_page.phon_number_field('effect')
        footer_page.Email_path_field('yeshuabel1427@gmail.com')
        footer_page.User_number_field('1212')
        footer_page.street_field('zehal-9')
        footer_page.city_field('sefad')
        assertion_error_text = self.driver.find_element(By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]").text
        assert assertion_error_text == "נא למלא שדה זה"

    @allure.description('new product of quantity')
    @pytest.mark.sanity
    def test_new_product_quantity(self):
        footer_page = footerLink(self)
        footer_page.login_to_the_system()
        time.sleep(5)
        footer_page.New_Product_add_field()


    @allure.description('new product of weirht')
    @pytest.mark.sanity
    def test_new_product_weight(self):
        driver = self.driver
        footer_page = footerLink(driver)
        # footer_page.open()
        footer_page.login_to_the_system()
        # footer_page.New_Product_add_field()
        # footer_page.weight_of_new_product()


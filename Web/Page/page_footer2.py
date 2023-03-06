import time
import pytest
import allure
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Web.Base.base_test import Base_test
from Web.Locators.footer2_locators import Locator_footer


class footerLink(Base_test, Locator_footer):

    a =Locator_footer

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        super().init()

    def navigate_t0_trado(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qa.trado.co.il/")
        # time.sleep(4)
        self.driver.implicitly_wait(10)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def footerLink(self):
        self.driver.find_element(By.XPATH, self.Cloth_button).click()
        self.driver.find_element(By.XPATH, self.Who_we_are).click()
        self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def who_we_are_link(self):
        self.driver.find_element(By.XPATH, self.Cloth_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Who_we_are).click()
        self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def More_details_link(self):
        self.driver.find_element(By.XPATH, self.More_detail).click()
        time.sleep(2)

    @allure.description('Scrolling')
    @pytest.mark.sanity
    def scroll_page_up(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        # self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def trading_link(self):
        self.driver.find_element(By.XPATH, self.trading).click()


    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def New_Order_Link(self):
        self.driver.find_element(By.XPATH, self.New_Order).click()
        time.sleep(2)
        # self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def E_torado_link(self):
        self.driver.find_element(By.XPATH, self.Cloth_button).click()
        self.driver.find_element(By.XPATH, self.E_torado).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Connected_etrado_button).click()
        self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def Busines_interface_link(self):
        self.driver.find_element(By.XPATH, self.Cloth_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Busines_interface).click()
        time.sleep(2)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def First_name_field(self, FirstNmae):
        self.driver.find_element(By.XPATH, self.First_name).clear()
        self.driver.find_element(By.XPATH, self.First_name).send_keys(FirstNmae)
        time.sleep(2)
        # self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def Last_name_field(self, LastName):
        self.driver.find_element(By.XPATH, self.Last_name).clear()
        self.driver.find_element(By.XPATH, self.Last_name).send_keys(LastName)
        time.sleep(2)

        # self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def HP_EM_field(self, HPNumber):
        self.driver.find_element(By.XPATH, self.HF_path).clear()
        self.driver.find_element(By.XPATH, self.HF_path).send_keys(HPNumber)
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def Business_name_field(self, Business):
        self.driver.find_element(By.XPATH, self.Busines_number).clear()
        self.driver.find_element(By.XPATH, self.Busines_number).send_keys(Business)
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def categories_field(self):
        self.driver.find_element(By.XPATH, self.Select_Categories).click()
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.step
    @allure.description('categoreis by cocktail')
    def categories_by_cocktail(self):
        sort = Select(self.driver.find_element(By.XPATH, self.Select_Categories))
        sort.select_by_visible_text('cocktail')
        time.sleep(2)

    @allure.step
    @allure.description('categories by resturant')
    def categories_by_resturant(self):
        sort = Select(self.driver.find_element(By.XPATH, self.Select_Categories))
        sort.select_by_visible_text("מסעדות")
        time.sleep(2)

    @allure.description('sdfghjk')
    @pytest.mark.sanity
    def phon_number_field(self, phoneNo):
        self.driver.find_element(By.XPATH, self.Phone_number).click()
        self.driver.find_element(By.XPATH, self.Phone_number).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Phone_number).send_keys(phoneNo)
        time.sleep(2)
        # self.driver.implicitly_wait(5)

    @allure.description('sdfghjk')
    @pytest.mark.sanity
    def Email_path_field(self, EMAIL):
        self.driver.find_element(By.XPATH, self.Email_path).clear()
        self.driver.find_element(By.XPATH, self.Email_path).send_keys(EMAIL)
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.description('sdfghjk')
    @pytest.mark.sanity
    def User_number_field(self, usenumber):
        self.driver.find_element(By.XPATH, self.User_numeber).clear()
        self.driver.find_element(By.XPATH, self.User_numeber).send_keys(usenumber)
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.description('sdfghjk')
    @pytest.mark.sanity
    def street_field(self, street):
        self.driver.find_element(By.XPATH, self.Enter_street).clear()
        self.driver.find_element(By.XPATH, self.Enter_street).send_keys(street)
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.description('sdfghjk')
    @pytest.mark.sanity
    def city_field(self, city):
        self.driver.find_element(By.XPATH, self.Enter_city).clear()
        self.driver.find_element(By.XPATH, self.Enter_city).send_keys(city)
        time.sleep(2)
        self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def submit_field(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()
        time.sleep(2)

        self.driver.implicitly_wait(5)

    @allure.description(' sdfghjk')
    @pytest.mark.sanity
    def enter_the_field_value1(self, F_name, L_name, HP_Em, business_name):
        self.First_name_field(F_name)
        self.Last_name_field(L_name)
        self.HP_EM_field(HP_Em)
        self.Business_name_field(business_name)

    @allure.description('error message')
    @pytest.mark.sanity
    def Error_massege_text(self):
        self.driver.find_element(By.XPATH, self.Error_massege).click()
        assertion_text = self.driver.find_element(By.XPATH, self.Error_massege)
        assert assertion_text == "נא למלא שדה זה"
        self.driver.implicitly_wait(5)

    # ********************************************************************************************************************


    # @allure.description('add new product ')
    # @pytest.mark.sanity
    # def new_phoneNumber_user(self):
    #     self.driver.find_element(By.XPATH, self.Telephon_login).click()
    #     time.sleep(2)

    @allure.description('add new product ')
    @pytest.mark.sanity
    def new_product_add_button(self):
        self.driver.find_element(By.XPATH, self.new_product_add).click()
        time.sleep(2)

    @allure.step
    @allure.description('add new product ')
    @pytest.mark.sanity
    def click_add_new_product(self):
        self.driver.find_element(By.CLASS_NAME, "verticalMenu_addProduct").click()
        self.driver.implicitly_wait(5)


    @allure.description('add new product ')
    @pytest.mark.sanity
    def New_Product_add_field(self):
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/form[1]/div[1]/div[1]/span[1]/input[1]").send_keys("1234")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/form[1]/div[1]/div[2]/span[1]/input[1]").send_keys("potato")
        time.sleep(3)
        self.driver.find_element(By.XPATH,  "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/form[1]/div[2]/div[2]/div[1]/div[2]/span[1]/input[1]").send_keys("40")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,  "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/form[1]/input[1]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/form[1]/div[2]/div[1]/div[1]/div[1]/span[1]/input[1]").send_keys("40")
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/form[1]/div[2]/div[1]/div[1]/div[2]/span[1]/input[1]").send_keys("120")
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/form[1]/div[2]/div[1]/div[1]/div[3]/span[1]/input[1]").send_keys('20')
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/form[1]/input[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/form[1]/div[2]/div[3]/div[1]/div[1]/span[1]/input[1]").send_keys('SADGDWTEFDGHVCSNBAC NBZCSCHSCGDVSHCDS  DVYWYVGEFHJW')
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/form[1]/input[1]").click()
        time.sleep(5)



    @allure.description('quantity of new product')
    @pytest.mark.sanity
    def quanity_of_new_product(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Quantit_carton_feild).send_keys("22")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Number_of_carton_instock).send_keys("34")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Minimu_carton_perOrder).send_keys("67")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Add_quantties).send_keys("15")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Collection_address).send_keys("44")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Anumber).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Add_comment).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Contact_name).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Street).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Entrance).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Floor).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Phone_number_field).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Add_collection).send_keys()
        self.driver.implicitly_wait(5)

    @allure.description('weight of product')
    @pytest.mark.sanity
    def weight_of_new_product(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.UnitOf_measur).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Average_weight_per_kg).send_keys()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Add_weight).send_keys()
        self.driver.implicitly_wait(5)

    def login_to_the_system(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button').click()
        self.driver.find_element(By.CLASS_NAME, "header_userAreaLink").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/input[1]").send_keys("0591111113")
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "form_submitBtn").click()
        time.sleep(1)
        cluster = "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority"
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['users']
        results = collection.find({"phone": '0591111113'})
        for resuit in results:
            login_code = (resuit['loginCode'])
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/input[1]").send_keys(
                login_code[0])
            time.sleep(1)
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/input[1]").click()
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/input[1]").send_keys(
                login_code[1])
            time.sleep(1)
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/input[1]").click()
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/input[1]").send_keys(
                login_code[2])
            time.sleep(1)
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/span[1]/input[1]").click()
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/span[1]/input[1]").send_keys(
                login_code[3])
            time.sleep(1)
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/span[1]/input[1]").click()
            self.driver.find_element(By.XPATH,
                                     "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/span[1]/input[1]").send_keys(
                login_code[4])
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]").click()
            time.sleep(3)
            self.driver.find_element(By.CLASS_NAME, "verticalMenu_addProduct").click()
            self.driver.implicitly_wait(5)
            # self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[3]/form[1]/div[1]/div[1]/span[1]/input[1]").send_keys("22")
            # self.driver.implicitly_wait(5)

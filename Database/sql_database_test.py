
from selenium import webdriver
import pyodbc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Web.Locators.new_sidebar_locators import SidebarLocators
import time

import pyodbc
# def test_data_entry():
x = SidebarLocators
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-CFNBSI63;'
                      'Database=Northwind;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Employees where EmployeeID = 1')


for i in cursor:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://qa.trado.co.il/contact")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, x.first_name_contact_xpath).send_keys(i[0])
    time.sleep(5)
    driver.find_element(By.XPATH, x.last_name_contact_xpath).send_keys(i[1])
    time.sleep(5)
    driver.find_element(By.ID, x.gmail_contact_path).send_keys(i[2])
    time.sleep(5)
    driver.find_element(By.ID, x.phone_contact_xpath).send_keys(i[3])
    time.sleep(3)
    driver.find_element(By.ID, x.message_field_xpath).send_keys(i[4])
    time.sleep(3)
    driver.find_element(By.ID, x.send_button_xpath).click()
    time.sleep(3)

    # driver.close()
#
#
# test_data_entry()

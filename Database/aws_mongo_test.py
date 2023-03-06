

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
website = "https://qa.trado.co.il/"
connection_className= "header_userAreaLink"
option1_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]'
option2_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]'
save = '//*[@id="root"]/div/div[4]/div/div/div/button'
login_facebook_button_className = 'login_facebook'
login_google_button_className = 'login_google'
login_twitter_button_className = 'login_twitter'
login_phone_input_xpath = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/input[1]"

def test_login():
    driver = webdriver.Chrome()
    driver.get(website)
    driver.maximize_window()
    driver.find_element(By.XPATH, option1_xpath).click()
    driver.find_element(By.XPATH, option2_xpath).click()
    driver.find_element(By.XPATH, save).click()
    driver.find_element(By.CLASS_NAME, connection_className).click()
    time.sleep(2)
    driver.find_element(By.XPATH, login_phone_input_xpath).send_keys("0591111113")
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "form_submitBtn").click()
    time.sleep(3)
    from pymongo import MongoClient

    cluster = "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority"
    db_client = MongoClient(cluster)
    db = db_client['trado_qa']
    collection = db['users']
    results = collection.find({"phone" : '0591111113'})
    for resuit in results:
        login_code = (resuit['loginCode'])
        driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/input[1]").send_keys(login_code[0])
        time.sleep(3)
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/input[1]").click()
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]/input[1]").send_keys(login_code[1])
        time.sleep(3)
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/input[1]").click()
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/span[1]/input[1]").send_keys(login_code[2])
        time.sleep(3)
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/span[1]/input[1]").click()
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/span[1]/input[1]").send_keys(login_code[3])
        time.sleep(3)
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/span[1]/input[1]").click()
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/span[1]/input[1]").send_keys(login_code[4])
        time.sleep(3)
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]").click()
        time.sleep(4)











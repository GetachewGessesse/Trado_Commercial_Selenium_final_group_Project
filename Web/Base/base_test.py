from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Base_test:

    service = Service("C:\\Users\\user\\Documents\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    def init(self):
        self.driver.get("https://qa.trado.co.il/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        return self.driver


import time

from appium import webdriver
from Mobile.DesiredCaps.desited_capabilities import DesiredCaps
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigate():
    desired_caps = DesiredCaps
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps.desired_caps)
    driver.get('https://qa-admin.trado.co.il/#/login')
    time.sleep(15)
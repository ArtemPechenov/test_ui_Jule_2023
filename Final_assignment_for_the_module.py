from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


URL='https://www.saucedemo.com/'
LOGIN1='standard_user'
LOGIN2='locked_out_user'
LOGIN3='problem_user'
LOGIN4='performance_glitch_user'
PASSWORD='secret_sauce'

def get_driver():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
return driver


def open_page(driver, URL):
    driver.get(URL)


def get_element_by_id(driver, locator):
return driver.find_element(By.ID, locator)


#def element_click(driver, locator):
    #element=get_element_by_id(driver, locator)
    #element.click()
    ##2 element_click(driver, 'login-link')
def element_send_keys():
element=get_element_by_id(driver, locator,text)
element.send_keys(text)

#1 Open
driver=get_driver()
open_page(driver)

#2,3 username/password
element_send_keys(driver,'name',LOGIN)
element_send_keys(driver,'name',PASSWORD)

#4 login-button
element_click(driver, 'login-button')

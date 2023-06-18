from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

URL='https://www.saucedemo.com/'
LOGIN1='standard_user'
LOGIN2='locked_out_user'
LOGIN3='problem_user'
LOGIN4='performance_glitch_user'
PASSWORD='secret_sauce'

#1 Open
driver.get(URL)

#2,3 username/password
input_username = driver.find_element(By.ID,'user-name')
input_password= driver.find_element(By.ID,'password')
input_username.send_keys(LOGIN1)
input_password.send_keys(PASSWORD)

#4 login-button
login_button= driver.find_element(By.ID,'login-button')
login_button.click()
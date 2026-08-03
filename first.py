import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID,"login-button")
login_button.click()


input("Press enter to close the brower..")

driver.quit()

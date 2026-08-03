import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com")

username = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"user-name")))
username.send_keys("standard_user")

password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
password.send_keys("secret_sauce")

login_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"login-button")))
login_button.click()


input("Press enter to close the brower..")

driver.quit()

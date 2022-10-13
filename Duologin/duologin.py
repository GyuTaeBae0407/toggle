import time 
import getpass
from concurrent.futures import thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

username_input = input("Username: ")
password_input = getpass.getpass(prompt="Password: ")


username_receieved = username_input
password_receieved = password_input

bcourses_url = "https://auth.berkeley.edu/cas/login?service=https%3A%2F%2Fcalcentral.berkeley.edu%2Fauth%2Fcas%2Fcallback%3Furl%3Dhttps%253A%252F%252Fcalcentral.berkeley.edu%252F"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome("/Users/baegy/Desktop/Caligram/chromedriver")
  

driver.get(bcourses_url)

username_input_driver = driver.find_element(By.ID, "username")
username_input_driver.send_keys(username_receieved)

password_input_driver = driver.find_element(By.ID, "password")
password_input_driver.send_keys(password_receieved)

driver.find_element(By.CSS_SELECTOR, "input.button").click()

time.sleep(10)
print("It has passed")

after_phone_url = driver.current_url
print(after_phone_url)
#driver.get(after_phone_url)
#driver.find_element(By.ID, "trust-browser-button").click()
#print("logged")
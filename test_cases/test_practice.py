from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
username = "admin"
password = "admin"
driver.get(f'https://{username}:{password}@the-internet.herokuapp.com/basic_auth')

sleep(3)

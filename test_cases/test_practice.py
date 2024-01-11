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

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
# from webdriver_manager.chrome import ChromeDriverManager
#
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# # Navigate to a page that requires authentication
# driver.get('https://the-internet.herokuapp.com/basic_auth')
#
# # Create an alert instance
# alert = Alert(driver)
#
# # Provide the username and password in the alert
# # For basic authentication, the format is "username:password"
# credentials = "admin:admin"
# alert.send_keys(credentials)
#
# # Accept the alert to proceed
# alert.accept()
#
# # Wait for some time to see the result (you can replace this with your actions)
# driver.implicitly_wait(5)
#
# # Close the browser window when finished
# driver.quit()


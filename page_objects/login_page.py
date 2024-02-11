from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    url = "http://127.0.0.1:8000/user/login/"
    username_input_id = "id_username"
    password_input_id = "id_password"
    sign_in_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/button"
    register_link_xpath = "/html/body/main/div/div/div/div/div[2]/div/small/a"
    title_xpath = "//*[@id='navbarColor01']/ul/li/h6"
    reset_password_xpath = "/html/body/main/div/div/div/div/div[2]/div/small/a"
    reset_password_link_text = "Reset Password"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.username_input_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def click_sign_in_btn(self):
        self.driver.find_element(By.XPATH, self.sign_in_btn_xpath).click()

    def click_sign_in(self):
        self.driver.find_element(By.XPATH, self.sign_in_btn_xpath).click()

    def click_on_reset_password_link(self):
        self.driver.find_element(By.XPATH, self.reset_password_xpath).click()

    def get_reset_password_url(self):
        try:
            link_element = self.driver.find_element(By.LINK_TEXT, self.reset_password_link_text)
        except NoSuchElementException:
            return None
        return link_element.get_attribute("href")

    def get_username_validation_msg(self):
        return self.driver.find_element(By.ID, self.username_input_id).get_attribute("validationMessage")

    def get_password_validation_msg(self):
        return self.driver.find_element(By.ID, self.password_input_id).get_attribute("validationMessage")

    def is_my_account_page_exists(self):
        try:
            return self.driver.find_element(By.XPATH, self.title_xpath).is_displayed()
        except Exception:
            return False

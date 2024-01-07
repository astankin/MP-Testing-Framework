from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterUserPage:
    register_url = "http://127.0.0.1:8000/user/register/"
    username_input_xpath = "//*[@id='id_username']"
    username_input_id = "id_username"
    email_input_id = "id_email"
    select_role_id = "id_role"
    password_input_id = "id_password1"
    conf_password_input_id = "id_password2"
    add_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/div[6]/button"
    confirmation_message_xpath = "/html/body/main/div/div/div/div/h3"
    username_error_msg = '//*[@id="error_1_id_username"]/strong'
    email_error_msg = "//*[@id='error_1_id_email']/strong"
    password_error_msg = "//*[@id='error_1_id_password2']/strong"
    cancel_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/div[6]/a"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.username_input_xpath).send_keys(username)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def set_confirm_password(self, conf_pass):
        self.driver.find_element(By.ID, self.conf_password_input_id).send_keys(conf_pass)

    def select_role(self, role):
        dropdown_element = self.driver.find_element(By.ID, self.select_role_id)
        select = Select(dropdown_element)
        select.select_by_visible_text(role)

    def click_add_btn(self):
        self.driver.find_element(By.XPATH, self.add_btn_xpath).click()

    def click_cancel_btn(self):
        self.driver.find_element(By.XPATH, self.cancel_btn_xpath).click()

    def get_confirm_message(self):
        return self.driver.find_element(By.XPATH, self.confirmation_message_xpath).text

    def get_username_error_msg(self):
        return self.driver.find_element(By.XPATH, self.username_error_msg)

    def get_email_error_msg(self):
        return self.driver.find_element(By.XPATH, self.email_error_msg)

    def get_username_validation_msg(self):
        return self.driver.find_element(By.ID, self.username_input_id).get_attribute("validationMessage")

    def get_email_validation_msg(self):
        return self.driver.find_element(By.ID, self.email_input_id).get_attribute("validationMessage")

    def get_conf_password_validation_msg(self):
        return self.driver.find_element(By.ID, self.conf_password_input_id).get_attribute("validationMessage")

    def get_password_error_msg(self):
        return self.driver.find_element(By.XPATH, self.password_error_msg)

    def register(self, username, email, role, password, conf_password):
        self.set_username(username)
        self.set_email(email)
        self.select_role(role)
        self.set_password(password)
        self.set_confirm_password(conf_password)
        self.click_add_btn()

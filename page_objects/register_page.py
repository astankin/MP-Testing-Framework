from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterUserPage:
    register_url = "http://127.0.0.1:8000/user/register/"
    username_input_xpath = "//*[@id='id_username']"
    username_input_id = "id_username"
    email_input_id = "id_email"
    first_name_id = "id_first_name"
    last_name_id = "id_last_name"
    select_role_id = "id_role"
    password_input_id = "id_password1"
    conf_password_input_id = "id_password2"
    add_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/div[8]/button"
    confirmation_message_xpath = "/html/body/main/div/div/div/div/h3"
    username_error_msg = '//*[@id="error_1_id_username"]/strong'
    firstname_error_msg = '//*[@id="error_1_id_first_name"]/strong'
    last_name_error_msg = '//*[@id="error_1_id_last_name"]/strong'
    email_error_msg = "//*[@id='error_1_id_email']/strong"
    password_error_msg = "//*[@id='error_1_id_password2']/strong"
    cancel_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/div[8]/a"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.username_input_xpath).send_keys(username)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)

    def set_first_name(self, f_name):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(l_name)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def set_confirm_password(self, conf_pass):
        self.driver.find_element(By.ID, self.conf_password_input_id).send_keys(conf_pass)

    def select_role(self, role):
        dropdown_element = self.driver.find_element(By.ID, self.select_role_id)
        select = Select(dropdown_element)
        select.select_by_visible_text(role)

    def click_add_btn(self):
        wait = WebDriverWait(self.driver, 10)
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.add_btn_xpath)))

        try:
            add_btn.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
            add_btn.click()

    def click_cancel_btn(self):
        wait = WebDriverWait(self.driver, 10)
        cancel_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancel_btn_xpath)))

        try:
            cancel_btn.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", cancel_btn)
            cancel_btn.click()

    def get_confirm_message(self):
        return self.driver.find_element(By.XPATH, self.confirmation_message_xpath).text

    def get_username_error_msg(self):
        return self.driver.find_element(By.XPATH, self.username_error_msg)

    def get_email_error_msg(self):
        return self.driver.find_element(By.XPATH, self.email_error_msg)

    def get_username_validation_msg(self):
        return self.driver.find_element(By.ID, self.username_input_id).get_attribute("validationMessage")

    def get_first_name_error_msg(self):
        return self.driver.find_element(By.XPATH, self.firstname_error_msg)

    def get_last_name_error_msg(self):
        return self.driver.find_element(By.XPATH, self.last_name_error_msg)

    def get_first_name_validation_msg(self):
        return self.driver.find_element(By.ID, self.first_name_id).get_attribute("validationMessage")

    def get_last_name_validation_msg(self):
        return self.driver.find_element(By.ID, self.last_name_id).get_attribute("validationMessage")

    def get_email_validation_msg(self):
        return self.driver.find_element(By.ID, self.email_input_id).get_attribute("validationMessage")

    def get_conf_password_validation_msg(self):
        return self.driver.find_element(By.ID, self.conf_password_input_id).get_attribute("validationMessage")

    def get_password_error_msg(self):
        return self.driver.find_element(By.XPATH, self.password_error_msg)

    def register(self, username, email, f_name, l_name, role, password, conf_password):
        self.set_username(username)
        self.set_email(email)
        self.set_first_name(f_name)
        self.set_last_name(l_name)
        self.select_role(role)
        self.set_password(password)
        self.set_confirm_password(conf_password)
        self.click_add_btn()

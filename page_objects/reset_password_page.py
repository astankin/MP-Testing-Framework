from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ResetPasswordPage:
    email_field_id = "id_email"
    request_pass_reset_btn = "/html/body/main/div/div/div/div/div[2]/form/button"
    url = "http://127.0.0.1:8000/user/password-reset/"
    confirm_message = "An email has been sent with instructions to reset your password"
    confirm_url = "http://127.0.0.1:8000/user/password-reset/done/"
    confirm_msg_xpath = "/html/body/main/div/div/div/div/h4"
    signin_btn_xpath = "//*[@id='sign_in_btn']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email)

    def click_reset_password_btn(self):
        self.driver.find_element(By.XPATH, self.request_pass_reset_btn).click()

    def click_signin_btn(self):
        self.driver.find_element(By.XPATH, self.signin_btn_xpath).click()

    def is_email_sent(self):
        try:
            conf_msg = self.driver.find_element(By.XPATH, self.confirm_msg_xpath).text
        except NoSuchElementException:
            conf_msg = None
        current_url = self.driver.current_url
        if current_url == self.confirm_url and conf_msg == self.confirm_message:
            return True
        return False


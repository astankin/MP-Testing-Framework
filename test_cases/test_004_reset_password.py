import os
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from page_objects.index_page import IndexPage
from page_objects.login_page import LoginPage
from page_objects.reset_password_page import ResetPasswordPage
from utilities.custom_logger import setup_logger
from utilities.email_generator import generate_random_email
from utilities.read_properties import ReadConfig


class TestResetPassword:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/reset_password.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    email = generate_random_email()
    path = os.path.abspath(os.curdir) + "\\test_data\\MP_Data.xlsx"
    invalid_emails = ["@yahoo.com", "john.doe.gmail.com", "john.doe@gmail",
                      "123456@cmail.com", "john.doe@1234565", "john.doe@1234565.com",
                      "456666@1234565.1234", "john@doe@1234565", "john doe@gmail.com"]

    def test_reset_password_with_valid_data(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.info("Launching application")
        self.driver.maximize_window()

        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

        self.logger.info("Click on reset password link")
        self.login_page = LoginPage(self.driver)
        self.login_page.click_on_reset_password_link()

        self.logger.info("Loading reset password page")
        self.reset_password_page = ResetPasswordPage(self.driver)
        self.reset_password_page.set_email(self.email)
        self.reset_password_page.click_reset_password_btn()

        if self.reset_password_page.is_email_sent():
            self.logger.info("Reset Password PASSED")
            assert True
        else:
            screenshot_dir = os.path.abspath(os.curdir) + "\\screenshots"
            screenshot_path = os.path.join(screenshot_dir, "test_account_register.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.info("Reset Password FAILED")
            assert False

    def test_reset_password_with_invalid_email(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.info("Launching application")
        self.driver.maximize_window()

        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

        self.logger.info("Click on reset password link")
        self.login_page = LoginPage(self.driver)
        self.login_page.click_on_reset_password_link()
        list_status = []
        invalid_emails = []
        self.logger.info("Loading reset password page")
        self.reset_password_page = ResetPasswordPage(self.driver)
        for email in self.invalid_emails:
            self.reset_password_page.set_email(email)
            self.reset_password_page.click_reset_password_btn()
            if not self.reset_password_page.is_email_sent():
                list_status.append("Pass")
            else:
                list_status.append("Fail")
                invalid_emails.append(email)
            self.reset_password_page.click_signin_btn()
            self.login_page.click_on_reset_password_link()

        if "Fail" in list_status:
            raise AssertionError(f"{', '.join(invalid_emails)} are not valid emails")
        else:
            assert True

    def test_reset_password_with_empty_email_field(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.info("Launching application")
        self.driver.maximize_window()

        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

        self.logger.info("Click on reset password link")
        self.login_page = LoginPage(self.driver)
        self.login_page.click_on_reset_password_link()

        self.logger.info("Loading reset password page")
        self.reset_password_page = ResetPasswordPage(self.driver)
        self.email = ""
        self.reset_password_page.set_email(self.email)
        self.reset_password_page.click_reset_password_btn()

        if self.reset_password_page.is_email_sent():
            self.logger.info("Reset Password Failed")
            raise AssertionError("The email field can NOT be empty")
        else:
            screenshot_dir = os.path.abspath(os.curdir) + "\\screenshots"
            screenshot_path = os.path.join(screenshot_dir, "test_account_register.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.info("Reset Password Passed")
            assert True

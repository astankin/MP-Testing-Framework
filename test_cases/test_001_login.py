import os.path
from time import sleep
import pytest
from selenium.common import NoSuchElementException

from page_objects.index_page import IndexPage
from page_objects.login_page import LoginPage
from utilities.custom_logger import setup_logger
from utilities.read_properties import ReadConfig


class TestLogin:
    base_url = ReadConfig.get_application_url()
    login_url = "http://127.0.0.1:8000/user/login/"
    logger = setup_logger(log_file_path='logs/register_account.log')

    username = ReadConfig.get_user()
    password = ReadConfig.get_password()
    invalid_username = "username"
    invalid_password = "Password12"

    def open_login_form(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

    def test_login_with_valid_credentials(self, setup):
        self.open_login_form(setup)
        self.logger.info("Providing customer details for login")
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_sign_in()

        target_page = self.login_page.is_my_account_page_exists()
        if target_page:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            assert False
        self.logger.info("**** End of the login test with correct data ****")

    def test_login_with_invalid_credentials(self, setup):
        self.open_login_form(setup)

        self.logger.info("Providing customer details for login")
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.invalid_username)
        self.login_page.set_password(self.invalid_password)
        self.login_page.click_sign_in()

        if self.driver.current_url == self.login_url:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            assert False
        self.logger.info("**** End of the login test with invalid data ****")

    def test_login_with_invalid_username(self, setup):
        self.open_login_form(setup)
        self.logger.info("Providing customer details for login")
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.invalid_username)
        self.login_page.set_password(self.password)
        self.login_page.click_sign_in()

        if self.driver.current_url == self.login_url:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            assert False
        self.logger.info("**** End of the login with invalid username ****")

    def test_login_with_invalid_password(self, setup):
        self.open_login_form(setup)

        self.logger.info("Providing customer details for login")
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.invalid_password)
        self.login_page.click_sign_in()

        if self.driver.current_url == self.login_url:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            assert False
        self.logger.info("**** End of the login with invalid password ****")

    def test_login_with_empty_username(self, setup):
        self.open_login_form(setup)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username("")
        self.login_page.set_password(self.password)
        self.login_page.click_sign_in()

        if self.driver.current_url == self.login_url:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            assert False

        expected_message = f"Please fill out this field."
        try:
            # Verify the validation message
            message = self.login_page.get_username_validation_msg()
            assert expected_message == message
        except NoSuchElementException:
            raise AssertionError("The username can NOT be empty!")
        self.logger.info("**** End of the login with invalid username ****")

    def test_login_with_empty_password(self, setup):
        self.open_login_form(setup)
        self.logger.info("Providing customer details for login")
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password("")
        self.login_page.click_sign_in()
        expected_message = f"Please fill out this field."
        if self.driver.current_url == self.login_url:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            assert False

        try:
            # Verify the validation message
            message = self.login_page.get_password_validation_msg()
            assert expected_message == message
        except NoSuchElementException:
            raise AssertionError("The password can NOT be empty!")

        self.logger.info("**** End of the login with empty password ****")

    def test_login_with_empty_username_and_password(self, setup):
        self.open_login_form(setup)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username("")
        self.login_page.set_password("")
        self.login_page.click_sign_in()
        expected_message = f"Please fill out this field."
        if self.driver.current_url == self.login_url:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\test_login.png")
            assert False

        try:
            # Verify the validation message
            message = self.login_page.get_password_validation_msg()
            assert expected_message == message
        except NoSuchElementException:
            raise AssertionError("The password can NOT be empty!")

        self.logger.info("**** End of the login with empty username and empty password ****")

    def test_reset_password_link(self, setup):
        expected_url = "http://127.0.0.1:8000/user/password-reset/"
        self.open_login_form(setup)
        self.login_page = LoginPage(self.driver)
        link = self.login_page.get_reset_password_url()
        if link:
            self.login_page.click_on_reset_password_link()
            assert self.driver.current_url == expected_url
        else:
            raise AssertionError("Link is not present on the page.")

    # def test_login_and_click_back_btn(self, setup):
    #     self.open_login_form(setup)
    #     self.logger.info("Providing customer details for login")
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.set_username(self.username)
    #     self.login_page.set_password(self.password)
    #     self.login_page.click_sign_in()
    #     self.driver.back()
    #     assert True

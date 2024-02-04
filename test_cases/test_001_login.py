import os.path
from time import sleep
import pytest

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

    def test_login_with_valid_data(self, setup):
        self.logger.info("**** Starting test_001_login ***")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

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

    def test_login_with_invalid_data(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

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
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

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
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("click on [Sign in]")
        self.index_page = IndexPage(self.driver)
        self.index_page.click_sign_in()

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

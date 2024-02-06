from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.logout_page import LogoutPage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.read_properties import ReadConfig


class TestLogout:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    confirm_msg = "You have been signed out!"

    def logout(self, setup):
        self.driver = setup
        open_form(self.driver, self.base_url, self.logger, self.login_username, self.login_password)
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_profile_link()
        self.homepage.click_on_logout_btn()
        self.logout_page = LogoutPage(self.driver)

    def test_logout(self, setup):
        self.logout(setup)
        conf_msg = self.logout_page.get_confirm_msg()
        assert conf_msg == self.confirm_msg
        assert self.driver.current_url == self.logout_page.url

    def test_logout_and_signin_again_link(self, setup):
        self.logout(setup)
        self.logout_page.click_signin_link()
        self.signin_page = LoginPage(self.driver)
        assert self.driver.current_url == self.signin_page.url

    def test_logout_and_signin_btn(self, setup):
        self.logout(setup)
        self.logout_page.click_signin_btn()
        self.signin_page = LoginPage(self.driver)
        assert self.driver.current_url == self.signin_page.url

    def test_logout_and_signin_again_homepage(self, setup):
        self.logout(setup)
        self.logout_page.click_signin_link()
        self.signin_page = LoginPage(self.driver)
        self.signin_page.set_username(self.login_username)
        self.signin_page.set_password(self.login_password)
        self.signin_page.click_sign_in_btn()
        assert self.driver.current_url == self.homepage.url

    def test_closing_the_browser_without_logout_and_loading__the_browser_again_should_stay_logged_in(self, setup):
        self.driver = setup
        open_form(self.driver, self.base_url, self.logger, self.login_username, self.login_password)
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_profile_link()
        sleep(3)
        self.driver.quit()
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(self.base_url)
        assert self.driver.current_url == self.homepage.url

    def test_logout_and_browsing_back(self, setup):
        self.logout(setup)
        self.driver.back()
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_equipment_list()
        assert self.driver.current_url == "http://127.0.0.1:8000/user/login/?next=/equipment/equipment-list/"

        self.driver.back()
        self.homepage.click_on_create_equipment()
        assert self.driver.current_url == "http://127.0.0.1:8000/user/login/?next=/equipment/create/"







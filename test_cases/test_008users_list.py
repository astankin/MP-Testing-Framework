import pytest
from page_objects.home_page import HomePage
from page_objects.user_info_modal import UserInfoModal
from page_objects.users_list_page import UsersListPage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.read_properties import ReadConfig


class TestUsersList:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    user_name = 'Atanas Stankin'
    username = 'nasko'
    email = 'a_stankin@abv.bg'

    def test_open_users_list_page(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_users_list()
        self.users_list_page = UsersListPage(self.driver)
        assert self.driver.current_url == self.users_list_page.url

    def test_modal_user_info(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_users_list()
        self.users_list_page = UsersListPage(self.driver)
        self.users_list_page.click_info_btn(tr_idx=1)
        self.modal = UserInfoModal(self.driver)
        name = self.modal.get_name(tr_idx=0, td_idx=1)
        username = self.modal.get_username(tr_idx=1, td_idx=1)
        email = self.modal.get_email(tr_idx=2, td_idx=1)
        assert name == self.user_name
        assert username == self.username
        assert email == self.email

    def test_modal_click_cancel_btn(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_users_list()
        self.users_list_page = UsersListPage(self.driver)
        self.users_list_page.click_info_btn(tr_idx=1)
        self.modal = UserInfoModal(self.driver)
        self.modal.click_cancel_btn()
        assert self.driver.current_url == self.users_list_page.url




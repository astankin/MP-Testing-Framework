import pytest

from page_objects.home_page import HomePage
from page_objects.users_list_page import UsersListPage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.read_properties import ReadConfig

base_url = ReadConfig.get_application_url()
logger = setup_logger(log_file_path='logs/register_account.log')
login_username = ReadConfig.get_user()
login_password = ReadConfig.get_password()


def test_clear_users_database(setup):
    # open_form(setup, base_url, logger, login_username, login_password)
    # home_page = HomePage(setup)
    # for _ in range(100):
    #     home_page.click_on_users_list()
    #     users_list_page = UsersListPage(setup)
    #     users_list_page.delete_user()
    pass

from time import sleep

import pytest

from page_objects.create_department_page import CreateDepartmentPage
from page_objects.department_page import DepartmentPage
from page_objects.home_page import HomePage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.read_properties import ReadConfig
from utilities.username_generator import generate_random_username


class TestCreateDepartment:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    department_name = generate_random_username(5)
    plant_index = 1
    success_url = "http://127.0.0.1:8000/plant/department-list/"
    current_url = "http://127.0.0.1:8000/plant/department/create/"

    def test_create_department(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_departments()
        self.department_page = DepartmentPage(self.driver)
        self.department_page.click_on_create_link()
        self.create_department_page = CreateDepartmentPage(self.driver)
        self.create_department_page.set_name(self.department_name)
        self.create_department_page.select_plant(self.plant_index)
        self.create_department_page.click_add_btn()
        assert self.driver.current_url == self.success_url
        assert self.department_page.get_last_created_plant_department() == self.department_name

    def test_create_department_with_empty_name_field(self, setup):
        self.department_name = ""
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_departments()
        self.department_page = DepartmentPage(self.driver)
        self.department_page.click_on_create_link()
        self.create_department_page = CreateDepartmentPage(self.driver)
        self.create_department_page.set_name(self.department_name)
        self.create_department_page.select_plant(self.plant_index)
        self.create_department_page.click_add_btn()
        assert self.driver.current_url == self.current_url

    def test_create_department_with_empty_plant(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_departments()
        self.department_page = DepartmentPage(self.driver)
        self.department_page.click_on_create_link()
        self.create_department_page = CreateDepartmentPage(self.driver)
        self.create_department_page.set_name(self.department_name)
        self.create_department_page.click_add_btn()
        assert self.driver.current_url == self.current_url

    def test_create_department_click_cancel(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_departments()
        self.department_page = DepartmentPage(self.driver)
        self.department_page.click_on_create_link()
        self.create_department_page = CreateDepartmentPage(self.driver)
        self.create_department_page.set_name(self.department_name)
        self.create_department_page.select_plant(self.plant_index)
        self.create_department_page.click_cancel_btn()
        assert self.driver.current_url == self.success_url


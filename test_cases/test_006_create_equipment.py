from time import sleep

import pytest

from page_objects.create_department_page import CreateDepartmentPage
from page_objects.create_equipment_page import CreateEquipmentPage
from page_objects.department_page import DepartmentPage
from page_objects.home_page import HomePage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.generate_random_number import generate_random_number
from utilities.generate_random_word import generate_random_word
from utilities.read_properties import ReadConfig
from utilities.username_generator import generate_random_username


class TestCreateDepartment:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    department_name = generate_random_username(5)
    success_url = "http://127.0.0.1:8000/equipment/equipment-list/"
    description = generate_random_username(9)
    equipment_type = "Machine"
    acquisition_date = "15-09-2018"
    acquisition_value = 50000
    currency = "BGN"
    year_of_manufacturing = 2005
    manufacturer = generate_random_word(7)
    model_number = generate_random_number()
    part_number = "LHM123465A-C"
    serial_number = "BGN1288393-989892-BM"
    plant = "BG20"
    department = "TSC"

    def test_create_equipment_with_valid_data(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup

        self.home_page = HomePage(self.driver)
        self.home_page.click_on_create_equipment()
        self.create_equipment_page = CreateEquipmentPage(self.driver)
        self.create_equipment_page.set_description(self.description)
        self.create_equipment_page.select_type(self.equipment_type)
        self.create_equipment_page.set_acquisition_date(self.acquisition_date)
        self.create_equipment_page.set_acquisition_value(self.acquisition_value)
        self.create_equipment_page.set_currency(self.currency)
        self.create_equipment_page.set_year_of_manufacturing(self.year_of_manufacturing)
        self.create_equipment_page.set_manufacturer(self.manufacturer)
        self.create_equipment_page.set_model_number(self.model_number)
        self.create_equipment_page.set_part_number(self.part_number)
        self.create_equipment_page.set_serial_number(self.serial_number)
        self.create_equipment_page.select_plant(self.plant)
        self.create_equipment_page.select_department(self.department)
        self.create_equipment_page.click_on_add_btn()
        assert self.success_url == self.driver.current_url

    def test_create_equipment_with_invalid_description(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.description = "invalid! description @#$%^"
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_create_equipment()
        self.create_equipment_page = CreateEquipmentPage(self.driver)
        self.create_equipment_page.set_description(self.description)
        self.create_equipment_page.select_type(self.equipment_type)
        self.create_equipment_page.set_acquisition_date(self.acquisition_date)
        self.create_equipment_page.set_acquisition_value(self.acquisition_value)
        self.create_equipment_page.set_currency(self.currency)
        self.create_equipment_page.set_year_of_manufacturing(self.year_of_manufacturing)
        self.create_equipment_page.set_manufacturer(self.manufacturer)
        self.create_equipment_page.set_model_number(self.model_number)
        self.create_equipment_page.set_part_number(self.part_number)
        self.create_equipment_page.set_serial_number(self.serial_number)
        self.create_equipment_page.select_plant(self.plant)
        self.create_equipment_page.select_department(self.department)
        self.create_equipment_page.click_on_add_btn()
        error_message = self.create_equipment_page.get_error_message()
        assert error_message == "Ensure this value contains only letters, numbers, and underscore."

    def test_create_equipment_with_empty_description(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.description = ""
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_create_equipment()
        self.create_equipment_page = CreateEquipmentPage(self.driver)
        self.create_equipment_page.set_description(self.description)
        self.create_equipment_page.select_type(self.equipment_type)
        self.create_equipment_page.set_acquisition_date(self.acquisition_date)
        self.create_equipment_page.set_acquisition_value(self.acquisition_value)
        self.create_equipment_page.set_currency(self.currency)
        self.create_equipment_page.set_year_of_manufacturing(self.year_of_manufacturing)
        self.create_equipment_page.set_manufacturer(self.manufacturer)
        self.create_equipment_page.set_model_number(self.model_number)
        self.create_equipment_page.set_part_number(self.part_number)
        self.create_equipment_page.set_serial_number(self.serial_number)
        self.create_equipment_page.select_plant(self.plant)
        self.create_equipment_page.select_department(self.department)
        self.create_equipment_page.click_on_add_btn()
        assert self.driver.current_url == self.create_equipment_page.url



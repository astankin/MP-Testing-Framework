from time import sleep

import psycopg2
import pytest

from page_objects.create_department_page import CreateDepartmentPage
from page_objects.create_plant_page import CreatePlantPage
from page_objects.edit_plant_page import EditPlantPage
from page_objects.home_page import HomePage
from page_objects.plant_list_page import PlantListPage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.get_db_data import GetData
from utilities.read_properties import ReadConfig


class TestPlantList:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    tr_idx = 2

    def test_open_plants_list_page(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_plants_list()
        self.plants_list_page = PlantListPage(self.driver)
        assert self.driver.current_url == self.plants_list_page.url

    def test_click_create_plant(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_plants_list()
        self.plants_list_page = PlantListPage(self.driver)
        self.plants_list_page.click_create_plant()
        self.create_plant_page = CreatePlantPage(self.driver)
        assert self.driver.current_url == self.create_plant_page.url

    def test_click_add_department(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_plants_list()
        self.plants_list_page = PlantListPage(self.driver)
        self.plants_list_page.click_add_department()
        self.create_department_page = CreateDepartmentPage(self.driver)
        assert self.driver.current_url == self.create_department_page.url

    def test_click_edit_plant(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_plants_list()
        self.plants_list_page = PlantListPage(self.driver)
        self.plants_list_page.click_edit_btn(self.tr_idx)
        assert self.driver.current_url == "http://127.0.0.1:8000/plant/update/1/"

    def test_plant_list(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_plants_list()
        self.plants_list_page = PlantListPage(self.driver)
        plants = self.plants_list_page.get_plants_info(1)
        db_plants = GetData().get_all_plants()
        assert len(plants) == len(db_plants)

        for i in range(len(db_plants)):
            assert plants[i] in db_plants

        for j in range(len(db_plants)):
            assert db_plants[j] in plants

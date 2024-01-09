from time import sleep

import pytest
from page_objects.edit_plant_page import EditPlantPage
from page_objects.home_page import HomePage
from page_objects.plant_list_page import PlantListPage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.generate_random_word import generate_random_word
from utilities.get_db_data import GetData
from utilities.read_properties import ReadConfig


class TestEditPlant:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    tr_idx = 2
    edit_plant_name = "LIEBHERR"
    plant_id = 54
    edit_city = "Dungannon"
    edit_address = "Edited Address"
    edit_cost_center = generate_random_word(3)

    def open_edit_plant_page(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_plants_list()
        self.plants_list_page = PlantListPage(self.driver)
        self.edit_plant_page = EditPlantPage(self.driver)
        self.edit_plant_page.open_edit_plant_page(self.plant_id)

    def test_edit_plant_name(self, setup):
        self.open_edit_plant_page(setup)
        self.edit_plant_page.edit_name(self.edit_plant_name)
        self.edit_plant_page.click_on_update_btn()
        edited_plant = self.plants_list_page.get_plants_info(1)[-1]
        assert edited_plant == self.edit_plant_name

    def test_edit_plant_country(self, setup):
        self.open_edit_plant_page(setup)
        self.edit_plant_page.edit_country(1)
        self.edit_plant_page.click_on_update_btn()
        edited_country = self.plants_list_page.get_plants_info(2)[-1]
        assert edited_country == "AF"

    def test_edit_plant_city(self, setup):
        self.open_edit_plant_page(setup)
        self.edit_plant_page.edit_city(self.edit_city)
        self.edit_plant_page.click_on_update_btn()
        edited_city = self.plants_list_page.get_plants_info(3)[-1]
        assert edited_city == "Dungannon"

    def test_edit_plant_address(self, setup):
        self.open_edit_plant_page(setup)
        self.edit_plant_page.edit_address(self.edit_address)
        self.edit_plant_page.click_on_update_btn()
        edited_address = self.plants_list_page.get_plants_info(4)[-1]
        assert edited_address == "Edited Address"

    def test_edit_plant_cost_center(self, setup):
        self.open_edit_plant_page(setup)
        self.edit_plant_page.edit_cost_center(self.edit_cost_center)
        self.edit_plant_page.click_on_update_btn()
        edited_cost_center = self.plants_list_page.get_plants_info(7)[-1]
        assert edited_cost_center == self.edit_cost_center

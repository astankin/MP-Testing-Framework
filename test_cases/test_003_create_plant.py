import os
import pytest
from page_objects.create_plant_page import CreatePlantPage
from page_objects.home_page import HomePage
from page_objects.plant_list_page import PlantListPage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.read_properties import ReadConfig
from utilities.username_generator import generate_random_username


class TestCreatePlant:
    base_url = ReadConfig.get_application_url()
    plant_list_url = "http://127.0.0.1:8000/plant/list/"
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    plant_name = generate_random_username(9)
    plant_country_idx = 5
    plant_address = ReadConfig.get_plant_address()
    plant_city = ReadConfig.get_plant_city()
    plant_cost_center = ReadConfig.get_plant_cost_center()

    def test_create_plant_with_valid_data(self, setup):
        self.logger.info("*** test_003_Create Plant ***")
        self.driver = setup
        open_form(self.driver, self.base_url, self.logger, self.login_username, self.login_password)
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_create_plant()
        self.creat_plant_page = CreatePlantPage(self.driver)
        self.creat_plant_page.create_plant(self.plant_name,
                                           self.plant_country_idx,
                                           self.plant_city,
                                           self.plant_address,
                                           self.plant_cost_center)
        self.plant_list_page = PlantListPage(self.driver)
        last_created_plant = self.plant_list_page.get_plants_info(1)[-1]
        assert self.driver.current_url == self.plant_list_url
        assert last_created_plant == self.plant_name
        self.logger.info("Creation of Plant PASSED")

    def test_create_plant_with_valid_data_click_cancel(self, setup):
        self.driver = setup
        open_form(self.driver, self.base_url, self.logger, self.login_username, self.login_password)
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_create_plant()
        self.plant_list_page = PlantListPage(self.driver)
        self.home_page.click_on_plants_list()
        last_created_plant = self.plant_list_page.get_plants_info(1)[-1]

        self.creat_plant_page = CreatePlantPage(self.driver)
        self.home_page.click_on_create_plant()
        self.creat_plant_page.set_name(self.plant_name)
        self.creat_plant_page.select_country(8)
        self.creat_plant_page.set_city(self.plant_city)
        self.creat_plant_page.set_address(self.plant_address)
        self.creat_plant_page.set_cost_center(self.plant_cost_center)
        self.creat_plant_page.click_cancel_btn()

        self.home_page.click_on_plants_list()
        last_plant = self.plant_list_page.get_plants_info(1)[-1]

        if last_created_plant == last_plant:
            self.logger.info("Registration PASSED")
            assert True
        else:
            screenshot_dir = os.path.abspath(os.curdir) + "\\screenshots"
            screenshot_path = os.path.join(screenshot_dir, "test_account_register.png")
            self.driver.save_screenshot(screenshot_path)
            self.logger.info("Registration FAILED")
            assert False

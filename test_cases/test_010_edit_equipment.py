from time import sleep

import pytest

from page_objects.edit_equipment_page import EditEquipmentPage
from page_objects.equipment_info_modal import EquipmentInfoPage
from page_objects.equipment_list_page import EquipmentListPage
from page_objects.home_page import HomePage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
from utilities.generate_random_number import generate_random_number
from utilities.read_properties import ReadConfig


class TestEditEquipment:
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()
    plant_id = 1
    description = "Edited Equipment"
    eq_type = {
        "Hand power tool": "Measuring tool",
        "Measuring tool": "Machine",
        "Machine": "Hand power tool",
    }
    new_value = generate_random_number()
    new_currency = "USD"
    new_year = "1983"
    new_manufacturer = "Edited Manufacturer"

    def open_edit_equipment_page(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_equipment_list()
        self.equipment_list_page = EquipmentListPage(self.driver)

    def test_edit_equipment_description(self, setup):
        self.open_edit_equipment_page(setup)
        eq_description = self.equipment_list_page.get_equipment_description()
        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page = EditEquipmentPage(setup)
        self.edit_equipment_page.clear_description_field()
        self.edit_equipment_page.set_description(self.description)
        self.edit_equipment_page.click_on_add_btn()
        edited_eq_description = self.equipment_list_page.get_equipment_description()
        assert edited_eq_description == self.description

        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page.clear_description_field()
        self.edit_equipment_page.set_description(eq_description)
        self.edit_equipment_page.click_on_add_btn()
        edited_eq_description = self.equipment_list_page.get_equipment_description()
        assert edited_eq_description == eq_description

    def test_edit_equipment_type(self, setup):
        self.open_edit_equipment_page(setup)
        eq_type = self.equipment_list_page.get_equipment_type()
        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page = EditEquipmentPage(setup)
        self.edit_equipment_page.select_type(self.eq_type[eq_type])
        self.edit_equipment_page.click_on_add_btn()
        edited_eq_type = self.equipment_list_page.get_equipment_type()
        assert edited_eq_type == self.eq_type[eq_type]

        eq_type = self.equipment_list_page.get_equipment_type()
        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page.select_type(self.eq_type[eq_type])
        self.edit_equipment_page.click_on_add_btn()
        edited_eq_type = self.equipment_list_page.get_equipment_type()
        assert edited_eq_type == self.eq_type[eq_type]

    def test_edit_acquisition_value(self, setup):
        self.open_edit_equipment_page(setup)
        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page = EditEquipmentPage(setup)
        self.edit_equipment_page.clear_value_field()
        self.edit_equipment_page.set_acquisition_value(self.new_value)
        self.edit_equipment_page.click_on_add_btn()
        self.equipment_list_page.click_info_btn()
        self.info_page = EquipmentInfoPage(setup)
        acq_value = self.info_page.get_value()
        self.info_page.click_close_btn()
        assert acq_value == f"{self.new_value:.2f} BGN"

    def test_edit_currency(self, setup):
        self.open_edit_equipment_page(setup)
        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page = EditEquipmentPage(setup)
        self.edit_equipment_page.set_currency(self.new_currency)
        self.edit_equipment_page.click_on_add_btn()
        self.equipment_list_page.click_info_btn()
        self.info_page = EquipmentInfoPage(setup)
        currency = self.info_page.get_currency()
        self.info_page.click_close_btn()
        assert currency == self.new_currency

    def test_edit_year_of_manufacturing(self, setup):
        self.open_edit_equipment_page(setup)
        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page = EditEquipmentPage(setup)
        self.edit_equipment_page.clear_year_field()
        self.edit_equipment_page.set_year_of_manufacturing(self.new_year)
        self.edit_equipment_page.click_on_add_btn()
        self.equipment_list_page.click_info_btn()
        self.info_page = EquipmentInfoPage(setup)
        year_of_man = self.info_page.get_year_of_manufacturing()
        self.info_page.click_close_btn()
        assert year_of_man == self.new_year

    @pytest.mark.current
    def test_edit_manufacturer(self, setup):
        self.open_edit_equipment_page(setup)
        self.equipment_list_page.click_edit_btn(self.plant_id)
        self.edit_equipment_page = EditEquipmentPage(setup)
        self.edit_equipment_page.clear_manufacturer_field()
        self.edit_equipment_page.set_manufacturer(self.new_manufacturer)
        self.edit_equipment_page.click_on_add_btn()
        self.equipment_list_page.click_info_btn()
        self.info_page = EquipmentInfoPage(setup)
        manufacturer = self.info_page.get_manufacturer()
        self.info_page.click_close_btn()
        assert manufacturer == self.new_manufacturer






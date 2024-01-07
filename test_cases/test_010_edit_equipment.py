from time import sleep

import pytest

from page_objects.edit_equipment_page import EditEquipmentPage
from page_objects.equipment_list_page import EquipmentListPage
from page_objects.home_page import HomePage
from test_cases.conftest import open_form
from utilities.custom_logger import setup_logger
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

    @pytest.mark.current
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






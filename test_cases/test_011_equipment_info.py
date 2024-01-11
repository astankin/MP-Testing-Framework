import pytest

from page_objects.equipment_info_modal import EquipmentInfoPage
from page_objects.equipment_list_page import EquipmentListPage
from page_objects.home_page import HomePage
from test_cases.conftest import open_form
from test_cases.test_010_edit_equipment import TestEditEquipment
from utilities.custom_logger import setup_logger
from utilities.read_properties import ReadConfig


class TestEquipmentInfo(TestEditEquipment):
    base_url = ReadConfig.get_application_url()
    logger = setup_logger(log_file_path='logs/register_account.log')
    login_username = ReadConfig.get_user()
    login_password = ReadConfig.get_password()

    def open_equipment_info_page(self, setup):
        open_form(setup, self.base_url, self.logger, self.login_username, self.login_password)
        self.driver = setup
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_equipment_list()
        self.equipment_list_page = EquipmentListPage(self.driver)
        self.equipment_list_page.click_info_btn()
        self.info_page = EquipmentInfoPage(setup)

    def test_equipment_type(self, setup):
        self.open_equipment_info_page(setup)
        eq_type = self.info_page.get_eq_type()
        assert eq_type in self.eq_type

    def test_equipment_manufacturer(self, setup):
        self.open_equipment_info_page(setup)
        manufacturer = self.info_page.get_manufacturer()
        assert manufacturer == self.new_manufacturer

    def test_equipment_model_number(self, setup):
        self.open_equipment_info_page(setup)
        model = self.info_page.get_model_number()
        assert model == self.new_model_num

    def test_equipment_year(self, setup):
        self.open_equipment_info_page(setup)
        year = self.info_page.get_year_of_manufacturing()
        assert year == self.new_year

    def test_equipment_serial_num(self, setup):
        self.open_equipment_info_page(setup)
        serial_num = self.info_page.get_serial_number()
        assert serial_num == self.new_serial_num

    def test_equipment_part_num(self, setup):
        self.open_equipment_info_page(setup)
        part_num = self.info_page.get_part_number()
        assert part_num == self.new_part_num

    def test_equipment_department(self, setup):
        self.open_equipment_info_page(setup)
        department = self.info_page.get_department()
        assert department == self.new_department

    def test_click_create_mp(self, setup):
        self.open_equipment_info_page(setup)
        self.info_page.click_create_mp()
        assert self.driver.current_url == f"http://127.0.0.1:8000/mp/create/{self.equipment_id}/"

    @pytest.mark.current
    def test_click_close_btn(self, setup):
        self.open_equipment_info_page(setup)
        self.info_page.click_close_btn()
        assert self.driver.current_url == self.equipment_list_page.url

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.create_equipment_page import CreateEquipmentPage


class EditEquipmentPage(CreateEquipmentPage):

    def __init__(self, driver):
        super().__init__(driver)

    def clear_description_field(self):
        self.driver.find_element(By.ID, self.description_id).clear()

    def clear_value_field(self):
        self.driver.find_element(By.ID, self.acquisition_value_id).clear()

    def clear_year_field(self):
        self.driver.find_element(By.ID, self.year_id).clear()

    def clear_manufacturer_field(self):
        self.driver.find_element(By.ID, self.manufacturer_id).clear()

    def clear_model_number_field(self):
        self.driver.find_element(By.ID, self.model_number_id).clear()

    def clear_part_number_field(self):
        self.driver.find_element(By.ID, self.part_number_id).clear()

    def clear_serial_number_field(self):
        self.driver.find_element(By.ID, self.serial_number_id).clear()




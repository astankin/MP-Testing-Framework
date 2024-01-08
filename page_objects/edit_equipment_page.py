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






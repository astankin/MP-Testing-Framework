from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateEquipmentPage:
    url = "http://127.0.0.1:8000/equipment/create/"
    description_id = "id_description"
    type_id = "id_type"
    acquisition_date_id = "id_acquisition_date"
    acquisition_value_id = "id_acquisition_value"
    currency_id = "id_currency_code"
    year_id = "id_year_of_manufacture"
    manufacturer_id = "id_manufacturer"
    model_number_id = "id_model_number"
    part_number_id = "id_part_number"
    serial_number_id = "id_serial_number"
    plant_id = "id_plant"
    department_id = "id_department"
    add_button_xpath = "/html/body/main/div/div/div/div/div[2]/form/button"
    error_msg = "/html/body/main/div/div/div/div/div[2]/form/ul[1]/li"

    def __init__(self, driver):
        self.driver = driver

    def set_description(self, description):
        self.driver.find_element(By.ID, self.description_id).send_keys(description)

    def select_type(self, type):
        dropdown_element = self.driver.find_element(By.ID, self.type_id)
        select = Select(dropdown_element)
        select.select_by_visible_text(type)

    def set_acquisition_date(self, date):
        self.driver.find_element(By.ID, self.acquisition_date_id).send_keys(date)

    def set_acquisition_value(self, value):
        self.driver.find_element(By.ID, self.acquisition_value_id).send_keys(value)

    def set_currency(self, currency):
        dropdown_element = self.driver.find_element(By.ID, self.currency_id)
        select = Select(dropdown_element)
        select.select_by_visible_text(currency)

    def set_year_of_manufacturing(self, year):
        self.driver.find_element(By.ID, self.year_id).send_keys(year)

    def set_manufacturer(self, manufacturer):
        self.driver.find_element(By.ID, self.manufacturer_id).send_keys(manufacturer)

    def set_model_number(self, model_number):
        self.driver.find_element(By.ID, self.model_number_id).send_keys(model_number)

    def set_part_number(self, part_number):
        self.driver.find_element(By.ID, self.part_number_id).send_keys(part_number)

    def set_serial_number(self, serial_number):
        self.driver.find_element(By.ID, self.serial_number_id).send_keys(serial_number)

    def select_plant(self, plant):
        dropdown_element = self.driver.find_element(By.ID, self.plant_id)
        select = Select(dropdown_element)
        select.select_by_visible_text(plant)

    def select_department(self, department):
        dropdown_element = self.driver.find_element(By.ID, self.department_id)
        select = Select(dropdown_element)
        select.select_by_visible_text(department)

    def click_on_add_btn(self):
        element = self.driver.find_element(By.XPATH, self.add_button_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def get_error_message(self):
        element = self.driver.find_element(By.XPATH, self.error_msg)
        return element.text

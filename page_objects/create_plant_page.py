from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreatePlantPage:
    url = "http://127.0.0.1:8000/plant/create/"
    name_input_id = "id_name"
    select_country_id = "id_country"
    city_input_id = "id_city"
    address_input_id = "id_address"
    cost_center_input_id = "id_cost_center"
    add_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/button"
    cancel_btn = "/html/body/main/div/div/div/div/div[2]/form/a"

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(By.ID, self.name_input_id).send_keys(name)

    def select_country(self, index):
        dropdown_element = self.driver.find_element(By.ID, self.select_country_id)
        select = Select(dropdown_element)
        select.select_by_index(index)

    def set_city(self, city):
        self.driver.find_element(By.ID, self.city_input_id).send_keys(city)

    def set_address(self, address):
        self.driver.find_element(By.ID, self.address_input_id).send_keys(address)

    def set_cost_center(self, cost_center):
        self.driver.find_element(By.ID, self.cost_center_input_id).send_keys(cost_center)

    def click_on_add_btn(self):
        self.driver.find_element(By.XPATH, self.add_btn_xpath).click()

    def click_cancel_btn(self):
        self.driver.find_element(By.XPATH, self.cancel_btn).click()

    def create_plant(self, name, index, city, address, cost_center):
        self.set_name(name)
        self.select_country(index)
        self.set_city(city)
        self.set_address(address)
        self.set_cost_center(cost_center)
        self.click_on_add_btn()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class EditPlantPage:
    url = "http://127.0.0.1:8000/plant/update/"
    name_input_id = "id_name"
    select_country_id = "id_country"
    city_input_id = "id_city"
    address_input_id = "id_address"
    cost_center_input_id = "id_cost_center"
    update_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/button"
    cancel_btn = "/html/body/main/div/div/div/div/div[2]/form/a"

    def __init__(self, driver):
        self.driver = driver

    def open_edit_plant_page(self, plant_id):
        self.driver.get(f"{self.url}{plant_id}")

    def edit_name(self, name):
        name_field = self.driver.find_element(By.ID, self.name_input_id)
        name_field.clear()
        name_field.send_keys(name)

    def edit_country(self, index):
        dropdown_element = self.driver.find_element(By.ID, self.select_country_id)
        select = Select(dropdown_element)
        select.select_by_index(index)

    def edit_city(self, city):
        city_field = self.driver.find_element(By.ID, self.city_input_id)
        city_field.clear()
        city_field.send_keys(city)

    def edit_address(self, address):
        address_field = self.driver.find_element(By.ID, self.address_input_id)
        address_field.clear()
        address_field.send_keys(address)

    def edit_cost_center(self, cost_center):
        cost_center_field = self.driver.find_element(By.ID, self.cost_center_input_id)
        cost_center_field.clear()
        cost_center_field.send_keys(cost_center)

    def click_on_update_btn(self):
        self.driver.find_element(By.XPATH, self.update_btn_xpath).click()

    def click_cancel_btn(self):
        self.driver.find_element(By.XPATH, self.cancel_btn).click()



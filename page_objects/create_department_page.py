from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateDepartmentPage:
    url = "http://127.0.0.1:8000/plant/department/create/"
    name_id = "id_name"
    plant_id = "id_plant"
    add_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/button"
    cancel_btn_xpath = "/html/body/main/div/div/div/div/div[2]/form/a"

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(By.ID, self.name_id).send_keys(name)

    def select_plant(self, index):
        dropdown_element = self.driver.find_element(By.ID, self.plant_id)
        select = Select(dropdown_element)
        select.select_by_index(index)

    def click_add_btn(self):
        self.driver.find_element(By.XPATH, self.add_btn_xpath).click()

    def click_cancel_btn(self):
        self.driver.find_element(By.XPATH, self.cancel_btn_xpath).click()
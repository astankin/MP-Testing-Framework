from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait


class EquipmentInfoPage:
    eq_id = 26
    table_xpath = f"//*[@id='myModal{eq_id}']/div/div/div[2]/table"
    table_row_xpath = ".//tr"
    eq_type_xpath = ".//tr[1]/td[2]"
    manufacturer_xpath = ".//tr[2]/td[2]"
    model_num_xpath = ".//tr[3]/td[2]"
    manuf_year_xpath = ".//tr[4]/td[2]"
    part_num_xpath = ".//tr[6]/td[2]"
    serial_number_xpath = ".//tr[5]/td[2]"
    department_xpath = ".//tr[7]/td[2]"
    create_mp_xpath = ".//tr[10]/td[2]/a"
    value_xpath = "//*[@id='myModal26']/div/div/div[2]/table/tbody/tr[9]/td[2]"
    close_btn_xpath = f"//*[@id='myModal{eq_id}']/div/div/div[3]/button"

    def __init__(self, driver):
        self.driver = driver
        self.modal = self.driver.switch_to.active_element

    def get_value(self):
        td = self.modal.find_element(By.XPATH, self.value_xpath)
        return td.text

    def click_close_btn(self):
        close_btn = self.modal.find_element(By.XPATH, self.close_btn_xpath)
        close_btn.click()

    def get_currency(self):
        currency = self.get_value().split()[1]
        return currency

    def get_department(self):
        department = self.modal.find_element(By.XPATH, self.department_xpath).text
        return department

    def get_year_of_manufacturing(self):
        year = self.modal.find_element(By.XPATH, self.manuf_year_xpath).text
        return year

    def get_manufacturer(self):
        manufacturer = self.modal.find_element(By.XPATH, self.manufacturer_xpath).text
        return manufacturer

    def get_model_number(self):
        model_number = self.modal.find_element(By.XPATH, self.model_num_xpath).text
        return model_number

    def get_part_number(self):
        part_number = self.modal.find_element(By.XPATH, self.part_num_xpath).text
        return part_number

    def get_serial_number(self):
        serial_number = self.modal.find_element(By.XPATH, self.serial_number_xpath).text
        return serial_number

    def get_eq_type(self):
        eq_type = self.modal.find_element(By.XPATH, self.eq_type_xpath).text
        return eq_type

    def click_create_mp(self):
        create_mp = self.modal.find_element(By.XPATH, self.create_mp_xpath)
        create_mp.click()
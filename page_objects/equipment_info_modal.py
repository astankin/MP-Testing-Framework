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


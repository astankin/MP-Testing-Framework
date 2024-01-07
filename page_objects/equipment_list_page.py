from selenium.webdriver.common.by import By


class EquipmentListPage:
    info_btn_xpath = "/html/body/main/div/div/div/div/div[2]/div/table/tbody/tr[9]/td[6]/button[1]"
    edit_btn_xpath = "/html/body/main/div/div/div/div/div[2]/div/table/tbody/tr"
    delete_btn_xpath = "/html/body/main/div/div/div/div/div[2]/div/table/tbody/tr[9]/td[6]/button[2]"
    table_xpath = "/html/body/main/div/div/div/div/div[2]/div/table"
    last_row_xpath = ".//tr"
    td_xpath = ".//td[2]"

    def __init__(self, driver):
        self.driver = driver

    def click_info_btn(self):
        pass

    def click_edit_btn(self, id):
        edit_btn = self.driver.find_element(By.XPATH, f"{self.edit_btn_xpath}[{id}]/td[6]/a")
        edit_btn.click()

    def get_equipment_description(self):
        table = self.driver.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.XPATH, self.last_row_xpath)
        last_row = rows[1]
        td = last_row.find_element(By.XPATH, self.td_xpath)
        return td.text

    def get_equipment_type(self):
        table = self.driver.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.XPATH, self.last_row_xpath)
        row = rows[1]
        td = row.find_element(By.XPATH, ".//td[3]")
        return td.text

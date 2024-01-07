from selenium.webdriver.common.by import By


class PlantListPage:
    url = "http://127.0.0.1:8000/plant/list/"
    table_xpath = "/html/body/main/div/div/div[2]/div/table"
    last_row_xpath = ".//tr"
    td_xpath = "/html/body/main/div/div/div[2]/div/table/tbody"
    add_department_xpath = "/html/body/main/div/div/div[2]/div/table/tbody/tr/td[6]/a"
    create_plant_xpath = "/html/body/main/div/div/div[2]/div/a"
    edit_plant_xpath = "/html/body/main/div/div/div[2]/div/table/tbody/tr"
    delete_plant_xpath = "/html/body/main/div/div/div[2]/div/table/tbody/tr/td[8]/button"

    def __init__(self, driver):
        self.driver = driver

    def get_plants_info(self, td_id):
        plants = []
        table = self.driver.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.XPATH, self.last_row_xpath)
        for i in range(1, len(rows)):
            td = rows[i].find_element(By.XPATH, f"{self.td_xpath}/tr[{i}]/td[{td_id}]")
            plants.append(td.text)
        return plants

    # def delete_plant(self):
    #     delete_btn = self.driver.find_element(By.XPATH, self.delete_plant_xpath)
    #     delete_btn.click()
    #     modal = self.driver.switch_to.active_element
    #     form = modal.find_element(By.TAG_NAME, 'form')
    #     form.submit()

    def click_create_plant(self):
        self.driver.find_element(By.XPATH, self.create_plant_xpath).click()

    def click_add_department(self):
        self.driver.find_element(By.XPATH, self.add_department_xpath).click()

    def click_edit_btn(self, index):
        self.driver.find_element(By.XPATH, f"{self.edit_plant_xpath}[{index}/td[8]/a]").click()

    def click_delete_btn(self):
        self.driver.find_element(By.XPATH, self.delete_plant_xpath).click()

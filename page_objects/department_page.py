from selenium.webdriver.common.by import By


class DepartmentPage:
    url = "http://127.0.0.1:8000/plant/department-list/"
    create_department_xpath = "/html/body/main/div/div/div[2]/div/a"
    table_xpath = "/html/body/main/div/div/div[2]/div/table"
    last_row_xpath = ".//tr"
    td_xpath = ".//td[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_create_link(self):
        self.driver.find_element(By.XPATH, self.create_department_xpath).click()

    def get_last_created_plant_department(self):
        table = self.driver.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.XPATH, self.last_row_xpath)
        last_row = rows[-1]
        td = last_row.find_element(By.XPATH, self.td_xpath)
        return td.text

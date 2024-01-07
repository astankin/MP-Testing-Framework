from selenium.webdriver.common.by import By


class UsersListPage:
    url = "http://127.0.0.1:8000/user/list/"
    table_xpath = "/html/body/main/div/div/div[2]/div/table"
    rows_xpath = ".//tr"
    td_xpath = ".//td[2]"
    info_btn_xpath = "/html/body/main/div/div/div[2]/div/table/tbody/tr"
    delete_btn_xpath = "/html/body/main/div/div/div[2]/div/table/tbody/tr[5]/td[7]/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def click_info_btn(self, tr_idx):
        info_btn = self.driver.find_element(By.XPATH, f"{self.info_btn_xpath}[{tr_idx}]/td[7]/button[1]")
        info_btn.click()

    def click_delete_btn(self):
        delete_btn = self.driver.find_element(By.XPATH, self.delete_btn_xpath)
        delete_btn.click()

    def delete_user(self):
        self.click_delete_btn()
        modal = self.driver.switch_to.active_element
        form = modal.find_element(By.TAG_NAME, 'form')
        form.submit()

    def get_last_created_user_name(self):
        table = self.driver.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.XPATH, self.rows_xpath)
        last_row = rows[-1]
        td = last_row.find_element(By.XPATH, self.td_xpath)
        return td.text

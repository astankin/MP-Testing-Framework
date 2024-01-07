from selenium.webdriver.common.by import By


class UserInfoModal:
    cancel_btn_xpath = '//*[@id="myModal1"]/div/div/div/div[2]/div/div[2]/div/button'
    table_xpath = "//*[@id='myModal1']/div/div/div/div[2]/div/div[2]/table"

    def __init__(self, driver):
        self.driver = driver
        self.modal = self.driver.switch_to.active_element

    def click_cancel_btn(self):
        cancel_btn = self.modal.find_element(By.XPATH, self.cancel_btn_xpath)
        cancel_btn.click()

    def get_name(self, tr_idx, td_idx):
        table = self.modal.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        name = rows[tr_idx].find_elements(By.TAG_NAME, 'td')[td_idx].text
        return name

    def get_username(self, tr_idx, td_idx):
        table = self.modal.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        username = rows[tr_idx].find_elements(By.TAG_NAME, 'td')[td_idx].text
        return username

    def get_email(self, tr_idx, td_idx):
        table = self.modal.find_element(By.XPATH, self.table_xpath)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        email = rows[tr_idx].find_elements(By.TAG_NAME, 'td')[td_idx].text
        return email

from selenium.webdriver.common.by import By


class LogoutPage:
    url = "http://127.0.0.1:8000/user/logout/"
    confirm_msg_xpath = "/html/body/main/div/div/div/div/h2"
    signin_again_link_xpath = "/html/body/main/div/div/div/div/div/a"
    signin_btn_id = "sign_in_btn"

    def __init__(self, driver):
        self.driver = driver

    def get_confirm_msg(self):
        return self.driver.find_element(By.XPATH, self.confirm_msg_xpath).text

    def click_signin_link(self):
        self.driver.find_element(By.XPATH, self.signin_again_link_xpath).click()

    def click_signin_btn(self):
        self.driver.find_element(By.ID, self.signin_btn_id).click()

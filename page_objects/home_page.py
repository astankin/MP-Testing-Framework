from selenium.webdriver.common.by import By


class HomePage:
    create_user_xpath = "//*[@id='sidebarMenu']/div/div/a[1]"
    users_list_xpath = "//*[@id='sidebarMenu']/div/div/a[2]"
    create_plant_xpath = "//*[@id='sidebarMenu']/div/div/a[3]"
    plants_list_xpath = "//*[@id='sidebarMenu']/div/div/a[4]"
    departments_xpath = "//*[@id='sidebarMenu']/div/div/a[5]"
    create_equipment_xpath = "//*[@id='sidebarMenu']/div/div/a[6]"
    equipment_list_xpath = "//*[@id='sidebarMenu']/div/div/a[8]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_create_user(self):
        button = self.driver.find_element(By.XPATH, self.create_user_xpath)
        self.driver.execute_script("arguments[0].click();", button)

    def click_on_users_list(self):
        button = self.driver.find_element(By.XPATH, self.users_list_xpath)
        self.driver.execute_script("arguments[0].click();", button)

    def click_on_create_plant(self):
        button = self.driver.find_element(By.XPATH, self.create_plant_xpath)
        self.driver.execute_script("arguments[0].click();", button)

    def click_on_plants_list(self):
        plants_button = self.driver.find_element(By.XPATH, self.plants_list_xpath)
        self.driver.execute_script("arguments[0].click();", plants_button)

    def click_on_departments(self):
        departments_button = self.driver.find_element(By.XPATH, self.departments_xpath)
        self.driver.execute_script("arguments[0].click();", departments_button)

    def click_on_create_equipment(self):
        create_equipment_btn = self.driver.find_element(By.XPATH, self.create_equipment_xpath)
        self.driver.execute_script("arguments[0].click();", create_equipment_btn)

    def click_on_equipment_list(self):
        equipment_list_btn = self.driver.find_element(By.XPATH, self.equipment_list_xpath)
        self.driver.execute_script("arguments[0].click();", equipment_list_btn)

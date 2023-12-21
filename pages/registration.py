from locators import RegistrationLocators
from selenium.webdriver.common.keys import Keys


class Registration:
    def __init__(self, driver) -> None:
        self.driver = driver

    def registration_click_button(self):
        self.driver.find_element(*RegistrationLocators.reg_btn).click()

    def name_input_data(self, name):
        self.driver.find_element(*RegistrationLocators.first_name).send_keys(name)

    def last_user_name_input_data(self, last):
        self.driver.find_element(*RegistrationLocators.last_name).send_keys(last)

    def user_mail_input(self, reg_mail):
        self.driver.find_element(*RegistrationLocators.regi_mail).send_keys(reg_mail)

    def password_input_data(self, reg_pwd):
        self.driver.find_element(*RegistrationLocators.regi_pwd).send_keys(reg_pwd)

    def password_confirm_input_data(self, reg_pwd_rep):
        self.driver.find_element(*RegistrationLocators.regi_repassw).send_keys(reg_pwd_rep)

    def select_region(self, region_name):
        selected_region = self.driver.find_element(*RegistrationLocators.region)
        selected_region.click()
        selected_region.send_keys(Keys.BACKSPACE * 8)
        selected_region.send_keys(region_name)

    def submit_button_click(self):
        self.driver.find_element(*RegistrationLocators.subm_btn).click()

    def registr_user(self, name: str,
                     last: str,
                     region_name: str,
                     reg_mail: str,
                     reg_pwd: str,
                     reg_pwd_rep: str) -> None:
        self.registration_click_button()
        self.name_input_data(name)
        self.last_user_name_input_data(last)
        self.user_mail_input(reg_mail)
        self.password_input_data(reg_pwd)
        self.password_confirm_input_data(reg_pwd_rep)
        self.select_region(region_name)
        self.submit_button_click()

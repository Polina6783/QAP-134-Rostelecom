from locators import AuthenticationLocators


class Authentication:
    def __init__(self, driver) -> None:
        self.driver = driver

    def login_input_data(self, query):
        self.driver.find_element(*AuthenticationLocators.user_name).send_keys(query)

    def password_input_data(self, value):
        self.driver.find_element(*AuthenticationLocators.user_pwd).send_keys(value)

    def login_button_click(self):
        self.driver.find_element(*AuthenticationLocators.log_btn).click()

    def help_button_click(self):
        self.driver.find_element(*AuthenticationLocators.help_btn).click()

    def agreement_link_click(self):
        self.driver.find_element(*AuthenticationLocators.agreement_link).click()

    def forgot_password_button_click(self):
        self.driver.find_element(*AuthenticationLocators.fgt_btn).click()

    def forward_button_click(self):
        self.driver.find_element(*AuthenticationLocators.forgot_forward).click()

    def login_user(self, query: str, value: str) -> None:
        self.login_input_data(query)
        self.password_input_data(value)
        self.login_button_click()

    def login_user_from_Belarus(self, query: str, value: str) -> None:
        self.login_input_data(query)
        self.password_input_data(value)

    def help_menu(self) -> None:
        self.help_button_click()

    def agreement_page(self) -> None:
        self.agreement_link_click()

    def empty_tel(self) -> None:
        self.forgot_password_button_click()
        self.forward_button_click()

    def wrong_tel(self, value) -> None:
        self.forgot_password_button_click()
        self.login_input_data(value)
        self.forward_button_click()


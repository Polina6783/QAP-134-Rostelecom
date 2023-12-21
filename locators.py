from selenium.webdriver.common.by import By


class AuthenticationLocators:
    reg_btn = (By.ID, "kc-register")
    user_name = (By.ID, "username")
    user_pwd = (By.ID, "password")
    log_btn = (By.ID, "kc-login")
    phone_tab = (By.ID, "t-btn-tab-phone")
    mail_tab = (By.ID, "t-btn-tab-mail")
    login_tab = (By.ID, "t-btn-tab-login")
    rmbr_chk = (By.XPATH, "a[@class='rt-checkbox__input']")
    help_btn = (By.XPATH, "//*[@id='faq-open']/a")
    agreement_link = (By.ID, "rt-auth-agreement-link")
    fgt_btn = (By.ID, "forgot_password")
    forgot_forward = (By.ID, "reset")


class RegistrationLocators:
    reg_btn = (By.ID, "kc-register")
    first_name = (By.CSS_SELECTOR, "*[name='firstName']")
    last_name = (By.CSS_SELECTOR, "*[name='lastName']")
    region = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[2]/div/div/input")
    region_name = (By.XPATH, "//*[text()='Новосибирская обл']")
    regi_mail = (By.ID, "address")
    regi_pwd = (By.ID, "password")
    regi_repassw = (By.ID, "password-confirm")
    subm_btn = (By.CSS_SELECTOR, "*[type='submit']")


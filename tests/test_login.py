from pages.authentication import Authentication
from tests_data import BASE_URL, DIFFERENT_URL, tel, pwd, inv_mail, oversize_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.by import By



def test_login(driver):
    page = Authentication(driver)
    page.login_user(tel, pwd)
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/main/div/div[2]/div[1]/div[2]/div[1]/div/span[2]/span")))

def test_invalid_mail(driver):
    page = Authentication(driver)
    page.login_user(inv_mail, pwd)
    # driver.save_screenshot("reg1.png")
    wrong_login = driver.find_element(By.ID, "form-error-message").text
    assert "Неверный логин или пароль" in wrong_login

def test_compare_tel_numbers(driver):
    page = Authentication(driver)
    page.login_user(tel, pwd)
    driver.get(DIFFERENT_URL)
    driver.implicitly_wait(3)
    driver.get(BASE_URL)
    user_page = driver.find_element(By.XPATH, "//*[@id='app']/main/div/div[2]/div[1]/div[2]/div[1]/div/span[2]/span").text
    assert tel in user_page
    

def test_logout(driver):
    page = Authentication(driver)
    remember_btn = driver.find_element(By.XPATH, "//*[@class='rt-checkbox__label']")
    remember_btn.click()
    page.login_user(tel, pwd)
    logout_btn = driver.find_element(By.ID, "logout-btn")
    logout_btn.click()
    auth_main_page = driver.find_element(By.XPATH, "//*[text()='Авторизация']").text
    assert 'Авторизация' in auth_main_page

def test_name_empty_field(driver):
    page = Authentication(driver)
    page.login_user('','')
    driver.save_screenshot("login_name_empty.png")
    allert_empty_fields = driver.find_element(By.XPATH, "//*[text()='Введите номер телефона']").text
    assert "Введите номер телефона" in allert_empty_fields

def test_help(driver):
    page = Authentication(driver)
    page.help_menu()
    WDW(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="faq-modal__content"]')))

def test_agreement(driver):
    page = Authentication(driver)
    page.agreement_page()
    driver.switch_to.window(driver.window_handles[1])
    WDW(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="offer-title"]')))

def test_empty_telephone_num(driver):
    page = Authentication(driver)
    page.empty_tel()
    message = driver.find_element(By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[2]/span").text
    assert "Введите номер телефона" in message

def test_wrong_telephone_num(driver):
    page = Authentication(driver)
    page.wrong_tel("1111")
    message = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span').text
    assert "Неверный формат телефона" in message

def test_captcha(driver):
    page = Authentication(driver)
    page.empty_tel()
    WDW(driver, timeout=3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '*[alt="Captcha"]')))

def test_forgot_password_captcha_refresh(driver):
    page = Authentication(driver)
    page.forgot_password_button_click()
    WDW(driver, timeout=10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '*[alt="Captcha"]')))
    captcha_first_link = page.driver.find_element(By.CSS_SELECTOR, '*[alt="Captcha"]').get_attribute('src')
    page.driver.find_element(By.CLASS_NAME, 'rt-captcha__reload').click()
    captcha_second_link = page.driver.find_element(By.CSS_SELECTOR, '*[alt="Captcha"]').get_attribute('src')
    assert captcha_first_link not in captcha_second_link

def test_max_char(driver):
    page = Authentication(driver)
    page.login_user(oversize_login, pwd)


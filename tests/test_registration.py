from pages.registration import Registration
from tests_data import reg_first_name, reg_last_name, reg_mail, reg_pwd, reg_pwd_rep, reg_region, test_pwd, invalid_mail, test_pwd_chars_oly, different_pwd, Chinese_char, Latin, Spec_char
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.by import By



def test_already_registred(driver):
    # переход на страницу и имитация регистрации с заполнением всех обязательных полей
    page = Registration(driver)
    page.registr_user(reg_first_name, reg_last_name, reg_region, reg_mail, reg_pwd, reg_pwd_rep )
    already_alert = driver.find_element(By.XPATH, "//*[text()='Учётная запись уже существует']").text
    assert "Учётная запись уже существует" in already_alert
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[name='firstName']")))

def test_empty_name(driver):
    page = Registration(driver)
    page.registr_user("", reg_last_name, reg_region, reg_mail, reg_pwd, reg_pwd_rep)
    error = driver.find_element(By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]').text
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[name='firstName']")))

def test_wrong_mail(driver):
    page = Registration(driver)
    page.registr_user(reg_first_name, reg_last_name, reg_region, invalid_mail, reg_pwd, reg_pwd_rep)
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.XPATH,'//*[text()="Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"]')))
    error = driver.find_element(By.XPATH,'//*[text()="Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"]').text
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' != (
        'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru') in error

def test_Chinese_char(driver):
    page = Registration(driver)
    page.registr_user(Chinese_char, reg_last_name, reg_region, reg_mail, reg_pwd, reg_pwd_rep)
    error = driver.find_element(By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]').text
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[name='firstName']")))

def test_Latin_char(driver):
    page = Registration(driver)
    page.registr_user(reg_first_name, Latin, reg_region, reg_mail, reg_pwd, reg_pwd_rep)
    error = driver.find_element(By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]').text
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[name='firstName']")))

def test_Spec_char(driver):
    page = Registration(driver)
    page.registr_user(reg_first_name, Latin, reg_region, Spec_char, reg_pwd, reg_pwd_rep)
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"]')))
    error = driver.find_element(By.XPATH, '//*[text()="Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"]').text
    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' != ('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru') in error

def test_password_lower_case(driver):
    page = Registration(driver)
    page.registr_user(reg_first_name, reg_last_name, reg_region, reg_mail, test_pwd, reg_pwd_rep)
    error = driver.find_element(By.XPATH, '//*[text()="Пароль должен содержать хотя бы одну заглавную букву"]').text
    assert "Пароль должен содержать хотя бы одну заглавную букву" in error
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[name='firstName']")))

def test_password_latin_chars_only(driver):
    page = Registration(driver)
    page.registr_user(reg_first_name, reg_last_name, reg_region, reg_mail, test_pwd_chars_oly, reg_pwd_rep)
    error = driver.find_element(By.XPATH, '//*[text()="Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"]').text
    assert "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру" in error
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[name='firstName']")))

def test_different_passwords(driver):
    page = Registration(driver)
    page.registr_user(reg_first_name, reg_last_name, reg_region, reg_mail, reg_pwd, different_pwd)
    error = driver.find_element(By.XPATH,'//*[text()="Пароли не совпадают"]').text
    assert "Пароли не совпадают" in error
    WDW(driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[name='firstName']")))






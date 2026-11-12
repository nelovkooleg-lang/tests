from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_yandex(driver, login, password):
    driver.get("https://yandex.ru")
    wait = WebDriverWait(driver, 10)

    # Ввод логина
    login_input = wait.until(EC.presence_of_element_located((By.ID, "passp-field-login")))
    login_input.send_keys(login)
    driver.find_element(By.ID, "passp:sign-in").click()

    # Ввод пароля
    password_input = wait.until(EC.presence_of_element_located((By.ID, "passp-field-passwd")))
    password_input.send_keys(password)
    driver.find_element(By.ID, "passp:sign-in").click()

    # Ожидание перехода в личный кабинет (проверка изменения URL)
    wait.until(EC.url_contains("id.yandex.ru"))
    return driver.current_url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_yandex(driver, login, password):
    driver.get("https://passport.yandex.ru/auth/")
    wait = WebDriverWait(driver, 10)

    # Ввод логина
    login_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="text-field-input"], [id="passp-field-login"]'))
    )
    login_input.clear()
    login_input.send_keys(login)
    submit_btn = wait.until(
        EC.element_to_be_clickable((BY.CSS_SELECTOR, '[data-testid="add-user-next"], [id="passp:sign-in"]'))
    )
    submit_btn.click()

    # Ввод пароля
    password_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="password-field-input"], [id="passp-field-passwd"]'))
    )
    password_input.clear()
    password_input.send_keys(password)
    sign_in_btn = wait.until(
        EC.element_to_be_clickable((BY.CSS_SELECTOR, '[data-testid="password-next"], [id="passp;sign-in"]'))
    )
    sign_in_btn.click()

    # Ожидание перехода в личный кабинет (проверка изменения URL)
    wait.until(EC.url_contains("id.yandex.ru"))
    return driver.current_url

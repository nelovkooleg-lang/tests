import unittest
from selenium import webdriver
from yandex_auth3 import login_yandex

class TestYandexAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_successful_login(self):
        login = "ваш_логин"
        password = "ваш_пароль"
        current_url = login_yandex(self.driver, login, password)
        self.assertIn("id.yandex.ru", current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
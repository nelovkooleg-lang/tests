import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from yandex_auth3 import login_yandex

LOGIN = os.getenv('YANDEX_LOGIN')
PASSWORD = os.getenv('YANDEX_PASSWORD')

class TestYandexAuth(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
    @unittest.skipUnless(LOGIN and PASSWORD, 'не заданы переменные окружения YANDEX_LOGIN и YANDEX_PASSWORD')
    def test_successful_login(self):
        current_url = login_yandex(self.driver, LOGIN, PASSWORD)
        self.assertIn("id.yandex.ru", current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

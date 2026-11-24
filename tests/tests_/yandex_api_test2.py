import os
import unittest
from yandex_api2 import create_folder, check_folder_exists, delete_folder

TOKEN = os.getenv('YANDEX_TOKEN')

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.folder_name = 'Test_Folder_Autotest'
        self.folder.path = f'disk:/{self.folder.name}'
        if TOKEN:
            delete_folder(TOKEN, self.folder_name)
    def tearDown(self):
        if TOKEN:
            delete_folder(TOKEN, self.folder_name)
    @unittest.skipUnless(TOKEN, 'не задана переменная окружения YANDEX_TOKEN')
    def test_create_folder_success(self):
        # 1. Создание новой папки (API возвращает 201 Created)
        status = create_folder(TOKEN, self.folder_name)
        self.assertEqual(status, 201)

        # 2. Проверка, что папка появилась (GET-запрос возвращает 200 OK)
        exists_status, data = check_folder_exists(TOKEN, self.folder_name)
        self.assertEqual(exists_status, 200)
        self.assertEqual(data.get('type'), 'dir')
        self.assertEqual(data.get('name'), self.folder_name)
        
    @unittest.skipUnless(TOKEN, 'не задана переменная окружения YANDEX_TOKEN')
    def test_create_folder_already_exists(self):
        # Отрицательный тест: попытка создать уже существующую папку (ошибка 409)
        create_folder(TOKEN, self.folder_name)
        status = create_folder(TOKEN, self.folder_name)
        self.assertEqual(status, 409)

    def test_create_folder_unauthorized(self):
        # Отрицательный тест: неверный токен (ошибка 401)
        status = create_folder("wrong_token_123", "Some_Folder")
        self.assertEqual(status, 401)

if __name__ == "__main__":
    unittest.main()

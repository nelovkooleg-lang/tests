import unittest
from yandex_api2 import create_folder, check_folder_exists

TOKEN = "ВАШ_ТОКЕН_ЯНДЕКС_ДИСКА"

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.folder_name = "Test_Folder_Autotest"

    def test_create_folder_success(self):
        # 1. Создание новой папки (API возвращает 201 Created)
        status = create_folder(TOKEN, self.folder_name)
        self.assertEqual(status, 201)

        # 2. Проверка, что папка появилась (GET-запрос возвращает 200 OK)
        exists_status = check_folder_exists(TOKEN, self.folder_name)
        self.assertEqual(exists_status, 200)

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
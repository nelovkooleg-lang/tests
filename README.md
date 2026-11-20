# Автотесты (Python, Pytest, Requests, Selenium)

Репозиторий с юнит-тестами, API-тестами Яндекс.Диска и UI-тестом авторизации Яндекс ID.

## Установка и настройка

1. Клонируйте репозиторий и создайте виртуальное окружение:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Задайте переменные окружения для запуска тестов Яндекс.Диска и Яндекс ID:
   ```bash
   # Windows (PowerShell):
   \$env:YANDEX_TOKEN="ваш_oauth_токен"
   \$env:YANDEX_LOGIN="ваш_логин"
   \$env:YANDEX_PASSWORD="ваш_пароль"

   # Linux/macOS:
   export YANDEX_TOKEN="ваш_oauth_токен"
   export YANDEX_LOGIN="ваш_логин"
   export YANDEX_PASSWORD="ваш_пароль"
   ```

## Запуск тестов

Выполните из корневой директории проекта:
```bash
pytest -v

import pytest
import requests
import yaml


@pytest.fixture(scope='session')
def auth_token():
    # Чтение данных из config.yaml
    with open("config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    # Адрес для запроса авторизации
    login_url = config['site_url'] + "/gateway/login"

    # Параметры для запроса авторизации
    payload = {
        "username": config['username'],
        "password": config['password']
    }

    # Отправка POST запроса для авторизации и получение токена
    response = requests.post(login_url, json=payload)

    # Проверка успешности запроса
    assert response.status_code == 200

    # Извлечение токена из ответа
    auth_token = response.json()['token']

    return auth_token

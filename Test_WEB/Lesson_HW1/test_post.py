import pytest
import requests
import yaml
from ddt import ddt, data, unpack


@ddt
class TestPosts:

    @data("notMe")
    def test_post_existence(self, owner, auth_token):
        # Чтение данных из config.yaml
        with open("config.yaml", 'r') as stream:
            config = yaml.safe_load(stream)

        # Адрес для запроса списка постов
        posts_url = config['site_url'] + "/api/posts"

        # Параметры для запроса списка постов
        headers = {
            "X-Auth-Token": auth_token
        }
        params = {
            "owner": owner
        }

        # Отправка GET запроса для получения списка постов другого пользователя
        response = requests.get(posts_url, headers=headers, params=params)

        # Проверка успешности запроса
        assert response.status_code == 200

        # Извлечение списка постов из ответа
        posts = response.json()['posts']

        # Проверка наличия поста с определенным заголовком
        expected_title = "Expected Post Title"
        assert any(post['title'] == expected_title for post in posts), f"Post with title '{expected_title}' not found"



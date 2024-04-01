import pytest
import yaml
from module import Site

with open('./testdata.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def set_locator3():
    return '''button'''


@pytest.fixture()
def set_locator4():
    return '''h2'''


@pytest.fixture()
def status_error():
    return '401'


@pytest.fixture()
def site():
    site_instance = Site(data['address'])
    yield site_instance
    site_instance.quit()


# Новая фикстура для предоставления данных для нового шага в тесте
@pytest.fixture()
def post_data():
    return {
        "title": "New Post Title",
        # Дополнительные данные для поста, если нужно
    }


@pytest.fixture()
def input_username():
    return '''h2'''


@pytest.fixture()
def post_button_locator():
    return '#create-btn'


@pytest.fixture()
def find_title():
    return '''//*[@id="create-item"]/div/div/div[7]/div/button/span'''


@pytest.fixture()
def login_success():
    return '''//*[@id="app"]/main/nav/a/span'''


@pytest.fixture()
def create_post_button_locator():
    return '#create-item > div > div > div:nth-child(7) > div > button > span'

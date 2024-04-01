import time
from telnetlib import EC

import yaml
import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from module import Site
from conftest import site


with open('./testdata.yaml') as f:
    data = yaml.safe_load(f)


site = Site(data['address'])


def test_1(site, set_locator1, set_locator2, set_locator3, set_locator4, status_error, login_success, post_button_locator, create_post_button_locator):
    selector1 = set_locator1
    imput1 = site.find_element('xpath', selector1)
    imput1.send_keys('secondone')
    selector2 = set_locator2
    imput2 = site.find_element('xpath', selector2)
    imput2.send_keys('bdefe21531')
    selector3 = set_locator3
    imput3 = site.find_element('css', selector3)
    imput3.click()
    # проверка, что вход успешен
    try:
        site.find_element('xpath', login_success)
    except NoSuchElementException:
        assert False, "Element with XPath '{}' not found after successful login".format(login_success)

        # Добавление поста после входа
    post_button = site.find_element('css', post_button_locator)
    post_button.click()
    time.sleep(5)
    # Ввод заголовка поста
    post_title_input = site.find_element('css', '#create-item > div > div > div:nth-child(1) > div > label > input')
    post_title_input.send_keys('Тестовый пост')
    # Нажатие кнопки "Создать пост, в моем варианте это 'Save'"
    create_post_button = site.find_element('css', create_post_button_locator)
    create_post_button.click()
    # Ожидание успешного создания поста
    time.sleep(5)
    # Проверка наличия созданного поста с заголовком, который указан выше
    try:
        post_title_element = site.find_element('xpath', f'//*[contains(text(), "Тестовый пост")]')
        assert post_title_element is not None, "Пост с заголовком 'Тестовый пост' не обнаружен после создания"
    except NoSuchElementException:
        assert False, "Пост с заголовком 'Тестовый пост' не обнаружен после создания"



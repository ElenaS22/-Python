import time
import pytest
import yaml
import requests
import logging
from testpage import OperationsHelper

with open('./datatest.yaml') as f:
    data = yaml.safe_load(f)


def test_get_authentication_token(browser):
    test_page = OperationsHelper(browser)
    auth_token = test_page.get_authentication_token()
    assert auth_token is not None, "Authentication failed"
    logging.info('Authentication token successfully obtained: %s', auth_token)


def test_get_posts_of_other_user(browser):
    test_page = OperationsHelper(browser)
    auth_token = test_page.get_authentication_token()  # Получение аутентификационного токена
    assert auth_token is not None, "Authentication failed"
    posts_response = test_page.get_posts_of_other_user(auth_token)  # Получение постов другого пользователя
    assert posts_response is not None, "Failed to retrieve posts of another user"
    logging.info('Successfully retrieved posts of another user.')


def test_web_operations(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(data['username'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()
    time.sleep(5)
    assert test_page.get_username_label() == f'Hello, secondone'
    test_page.click_contact_us()
    time.sleep(5)
    assert test_page.get_success_contact() == f'Contact us!'
    test_page.enter_cont_name(data['content_name'])
    test_page.enter_cont_email(data['content_email'])
    test_page.enter_cont_content(data['content_text'])
    test_page.click_contact_btn()
    time.sleep(5)
    test_page.get_alert()
    time.sleep(5)
    assert test_page.get_alert() == f'Form successfully submitted'


if __name__ == '__main':
    pytest.main(['-vv'])

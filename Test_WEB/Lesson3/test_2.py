import time
from telnetlib import EC
import pytest
import yaml
import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from module import Site
from testpage import OperationsHelper

with open('./datatest.yaml') as f:
    data = yaml.safe_load(f)
    status_error = data['status_error']
    address = data['address']
    username = data['username']
    password = data['password']


def test_positive(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(username)
    test_page.enter_pass(password)
    test_page.click_login_button()
    time.sleep(10)
    assert test_page.get_username_label() == f'Hello, secondone'
    test_page.get_contact_us()
    time.sleep(5)
    assert test_page.find_success_contact() == f'Contact us!'
    test_page.enter_cont_name('test')
    test_page.enter_cont_email('test@test.ru')
    test_page.enter_cont_content('something about')
    test_page.click_contact_btn()
    time.sleep(5)
    test_page.find_alert()
    assert test_page.find_alert() == f'Form successfully submitted'




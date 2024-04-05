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
    assert test_page.get_username_lable() == f'Hello, secondone'


def test_contact_us_form(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    # Assuming the Contact Us link is located using a specific locator
    contact_us_link_locator = (By.XPATH, '//*[@id="contact-us-link"]')
    contact_us_form_locator = (By.ID, 'contact-us-form')  # Adjust the locator as per your actual HTML structure
    # Click on the Contact Us link
    test_page.find_element(contact_us_link_locator).click()
    # Wait until the Contact Us form is visible
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(contact_us_form_locator))
    # Fill in the form fields
    test_page.enter_contact_us_details()  # Assuming you have a method to enter contact details
    # Click on the submit button
    submit_button_locator = (By.ID, 'submit-button')  # Adjust the locator as per your actual HTML structure
    test_page.find_element(submit_button_locator).click()
    # Switch to alert and get text
    alert = browser.switch_to.alert
    alert_text = alert.text
    # Verify the alert text
    assert "Your message has been submitted" in alert_text

if __name__ == '__main__':
    pytest.main(['vv'])

'''
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


'''

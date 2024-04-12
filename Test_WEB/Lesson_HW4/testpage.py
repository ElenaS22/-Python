import logging
from BaseApp import BasePage
import requests
from requests.exceptions import HTTPError
from selenium.webdriver.common.by import By
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = By.XPATH, locators["xpath"][locator]
    for locator in locators["css"].keys():
        ids[locator] = By.CSS_SELECTOR, locators["css"][locator]


class OperationsHelper(BasePage):

    # enter text into field
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We found text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_authentication_token(self):
        with open('datatest.yaml', 'r') as f:
            data = yaml.safe_load(f)

        login_url = data['address']
        payload = {
            'username': data['username'],
            'password': data['password']
        }
        try:
            logging.debug('Sending POST request to login URL: %s', login_url)
            response = requests.post(login_url, json=payload)
            response.raise_for_status()
            logging.debug('Received response from login URL: %s', response.text)

            content_type = response.headers.get('content-type')
            if 'application/json' not in content_type:
                raise ValueError('Unexpected content type: {}'.format(content_type))

            response_json = response.json()
            auth_token = response_json.get('token')
            if auth_token is None:
                raise ValueError('Authentication token not found in response')

            posts_url = 'https://test-stand.gb.ru/api/posts'
            params = {
                'sort': 'createdAt',
                'order': 'ASC',
                'owner': 'notMe'
            }
            headers = {
                'X-Auth-Token': auth_token
            }
            logging.debug('Sending GET request to posts URL: %s', posts_url)
            posts_response = requests.get(posts_url, headers=headers, params=params)
            posts_response.raise_for_status()
            logging.debug('Received response from posts URL: %s', posts_response.text)

        except requests.exceptions.RequestException as req_err:
            logging.error('An error occurred during request: %s', req_err)
        except ValueError as val_err:
            logging.error('Value error occurred: %s', val_err)
        except Exception as err:
            logging.error('Other error occurred: %s', err)
        else:
            logging.info('Authentication token successfully obtained: %s', auth_token)

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_cont_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME"], word, description="content name form")

    def enter_cont_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL"], word, description="content email form")

    def enter_cont_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content text form")

    # click to buttons

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_contact_us(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US"], description="contact")

    def click_contact_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="send contact")

    #def click_new_post_btn(self):
    #self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description="new post create")

    # get some errors or info

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="Error label")

    def get_username_label(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POSITIVE_ENTER"], description="Success login")

    def get_success_contact(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_SUCCESS_CONTACT"], description="Success cont")

    def get_alert(self):
        logging.info("Get alert text")
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert_text


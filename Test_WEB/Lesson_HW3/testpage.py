import logging

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_POSITIVE_ENTER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_SUCCESS_CONTACT = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")



class OperationsHelper(BasePage):

    def enter_login(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=5)
        text = error_field.text
        logging.info(f'We found text {text} in {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_username_lable(self):
        label_field = self.find_element(TestSearchLocators.LOCATOR_POSITIVE_ENTER, time=5)
        text = label_field.text
        logging.info(f'We found text {text} in {TestSearchLocators.LOCATOR_POSITIVE_ENTER[1]}')
        return text


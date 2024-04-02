import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('./testdata.yaml') as f:
    data = yaml.safe_load(f)

browser = data["browser"]


class Site:
    def __init__(self, address):
        if browser == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(data["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def click_button(self, mode, path):
        button = self.find_element(mode, path)
        button.click()

    def fill_post_form(self, title, content):
        title_input = self.find_element('css', 'input#post-title')
        title_input.send_keys(title)

        content_input = self.find_element('css', 'textarea#post-content')
        content_input.send_keys(content)

    def submit_post(self):
        submit_button = self.find_element('css', 'button#submit-post')
        submit_button.click()
    def quit(self):
        self.driver.quit()

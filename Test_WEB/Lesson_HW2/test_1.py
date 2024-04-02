from telnetlib import EC

import yaml
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from module import Site
from conftest import site

with open('./testdata.yaml') as f:
    data = yaml.safe_load(f)

site = Site(data['address'])


def test_1(site, set_locator1, set_locator2, set_locator3, set_locator4, status_error, login_success):
    selector1 = set_locator1
    imput1 = site.find_element('xpath', selector1)
    imput1.send_keys('secondone')
    selector2 = set_locator2
    imput2 = site.find_element('xpath', selector2)
    imput2.send_keys('bdefe21531')
    selector3 = set_locator3
    imput3 = site.find_element('css', selector3)
    imput3.click()
    site.driver.find_element_by_xpath(login_success)
    selector4 = set_locator4
    find1 = site.find_element('css', selector4)
    assert find1.text == status_error


import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        with allure.step('open'):
            self.browser.get(self.url)

    def back(self):
        with allure.step('back'):
            self.browser.back()

    def refresh(self):
        with allure.step('refresh'):
            self.browser.refresh()

    def correct_url(self, link):
        with allure.step('correct_url'):
            assert self.browser.current_url == link, f'УРЛ не совпадает'

    def click(self, how, what):
        with allure.step('click'):
            WebDriverWait(self.browser, 10, 1, TimeoutException).until(EC.element_to_be_clickable((how, what)))
            self.browser.find_element(how, what).click()

    def is_element_present(self, how, what):
        with allure.step('is_element_present'):
            try:
                self.browser.find_element(how, what)
            except NoSuchElementException:
                return False
            return True

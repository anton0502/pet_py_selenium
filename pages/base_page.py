from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def back(self):
        self.browser.back()

    def refresh(self):
        self.browser.refresh()

    def correct_url(self, link):
        assert self.browser.current_url == link, f'УРЛ не совпадает'

    def click(self, how, what):
        WebDriverWait(self.browser, 10, 1, TimeoutException).until(EC.element_to_be_clickable((how, what)))
        self.browser.find_element(how, what).click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True

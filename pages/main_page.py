from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_correct_url(self):
        url = self.browser.current_url
        assert url == 'http://automationpractice.com/index.php', f'УРЛ не совпадает'

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page_url(self):
        self.correct_url(link='https://demoqa.com/')

    def should_open_main_page_by_logo_click(self):
        assert self.is_element_present(*MainPageLocators.MAIM_PAGE_LOGO_LINK), f'лого пропало'
        self.click(*MainPageLocators.MAIM_PAGE_LOGO_LINK)

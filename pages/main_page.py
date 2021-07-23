from pages.base_page import BasePage
from pages.locators import MainPageLocators
import allure


class MainPage(BasePage):
    def should_be_main_page_url(self):
        with allure.step('should_be_main_page_url'):
            self.correct_url(link='https://demoqa.com/')

    def should_open_main_page_by_logo_click(self):
        with allure.step('should_open_main_page_by_logo_click'):
            assert self.is_element_present(*MainPageLocators.MAIM_PAGE_LOGO_LINK), f'лого пропало'
            self.click(*MainPageLocators.MAIM_PAGE_LOGO_LINK)

    def should_open_elements(self):
        with allure.step('should_open_elements'):
            assert self.is_element_present(*MainPageLocators.ELEMENTS_LIST), f'список элементов пропал'
            self.click(*MainPageLocators.ELEMENTS_LIST)
            self.correct_url(link='https://demoqa.com/elements')

    def should_open_forms(self):
        with allure.step('should_open_forms'):
            assert self.is_element_present(*MainPageLocators.FORMS_LIST), f'список форм пропал'
            self.click(*MainPageLocators.FORMS_LIST)
            self.correct_url(link='https://demoqa.com/forms')

    def should_open_alerts(self):
        with allure.step('should_open_alerts'):
            assert self.is_element_present(*MainPageLocators.ALERTS_LIST), f'список алертов пропал'
            self.click(*MainPageLocators.ALERTS_LIST)
            self.correct_url(link='https://demoqa.com/alertsWindows')

    def should_open_widgets(self):
        with allure.step('should_open_widgets'):
            assert self.is_element_present(*MainPageLocators.WIDGETS_LIST), f'список виджетов пропал'
            self.click(*MainPageLocators.WIDGETS_LIST)
            self.correct_url(link='https://demoqa.com/widgets')

    def should_open_interactions(self):
        with allure.step('should_open_interactions'):
            assert self.is_element_present(*MainPageLocators.INTERACTIONS_LIST), f'список взаимодействий пропал'
            self.click(*MainPageLocators.INTERACTIONS_LIST)
            self.correct_url(link='https://demoqa.com/interaction')

    def should_open_book_store(self):
        with allure.step('should_open_book_store'):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            assert self.is_element_present(*MainPageLocators.BOOK_STORE_LIST), f'книжный маназин пропал'
            self.click(*MainPageLocators.BOOK_STORE_LIST)
            self.correct_url(link='https://demoqa.com/books')

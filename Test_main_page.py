from pages.main_page import MainPage
from allure_commons.types import AttachmentType
import allure
import pytest

link = "https://demoqa.com/"


@allure.feature('MainPage')
def test_main_page_url(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_page_url()


@allure.feature('MainPage')
def test_logo_click(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_open_main_page_by_logo_click()
    page.should_be_main_page_url()


class TestLists:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, link)
        page.open()

    @allure.feature('TestListsElements')
    @allure.story('ElementsLink')
    def test_elements_link(self, browser):
        page = MainPage(browser, link)
        with allure.step('Main page is open'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
        page.should_open_elements()
        with allure.step('Elements link is good'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('TestListsElements')
    @allure.story('FormsLink')
    def test_forms_link(self, browser):
        page = MainPage(browser, link)
        with allure.step('Main page is open'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
        page.should_open_forms()
        with allure.step('Forms link is good'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('TestListsElements')
    @allure.story('AlertsLink')
    def test_alerts_link(self, browser):
        page = MainPage(browser, link)
        with allure.step('Main page is open'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
        page.should_open_alerts()
        with allure.step('Alerts link is good'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('TestListsElements')
    @allure.story('WidgetsLink')
    def test_widgets_link(self, browser):
        page = MainPage(browser, link)
        with allure.step('Main page is open'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
        page.should_open_widgets()
        with allure.step('Widgets link is good'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('TestListsElements')
    @allure.story('InteractionsLink')
    def test_interactions_link(self, browser):
        page = MainPage(browser, link)
        with allure.step('Main page is open'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
        page.should_open_interactions()
        with allure.step('Interactions link is good'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('TestListsElements')
    @allure.story('BookStoreLink')
    def test_book_store_link(self, browser):
        page = MainPage(browser, link)
        with allure.step('Main page is open'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
        page.should_open_book_store()
        with allure.step('Book store link is good'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

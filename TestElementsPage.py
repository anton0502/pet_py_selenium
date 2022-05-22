from pages.elements_page import ElementsPage
from allure_commons.types import AttachmentType
import allure
import pytest

link = "https://demoqa.com/elements"


class TestElementsList:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = ElementsPage(browser, link)
        page.open()

    @allure.feature('ElementPage')
    @allure.story('TextBox')
    def test_text_box_tab(self, browser):
        page = ElementsPage(browser, link)
        page.should_open_text_box_tab()
        page.should_contain_all_text_box_fields()
        with allure.step('Text tab is opened'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('ElementPage')
    @allure.story('TextBox')
    def test_fill_text_box_tab_and_submit_form(self, browser):
        page = ElementsPage(browser, link)
        page.should_fill_all_text_box_fields()
        with allure.step('Text tab fields is filled'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)
        page.should_submit_form()
        with allure.step('Text tab form is submitted'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screenshot', attachment_type=AttachmentType.PNG)

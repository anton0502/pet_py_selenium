from pages.main_page import MainPage
import pytest

link = "https://demoqa.com/"


@pytest.mark.base_page
def test_main_page_url(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_page_url()


@pytest.mark.base_page
def test_logo_click(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_open_main_page_by_logo_click()
    page.should_be_main_page_url()


@pytest.mark.base_page
@pytest.mark.lists
class TestLists:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, link)
        page.open()

    def test_elements_link(self, browser):
        page = MainPage(browser, link)
        page.should_open_elements()

    def test_forms_link(self, browser):
        page = MainPage(browser, link)
        page.should_open_forms()

    def test_alerts_link(self, browser):
        page = MainPage(browser, link)
        page.should_open_alerts()

    def test_widgets_link(self, browser):
        page = MainPage(browser, link)
        page.should_open_widgets()

    def test_interactions_link(self, browser):
        page = MainPage(browser, link)
        page.should_open_interactions()

    def test_book_store_link(self, browser):
        page = MainPage(browser, link)
        page.should_open_book_store()

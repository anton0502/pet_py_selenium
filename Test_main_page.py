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

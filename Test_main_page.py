from pages.main_page import MainPage
import pytest

link = "http://automationpractice.com/"


@pytest.mark.base_page
def test_main_page_url(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_correct_url()

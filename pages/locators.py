from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class MainPageLocators:
    MAIM_PAGE_LOGO_LINK = (By.CSS_SELECTOR, 'header > a')
    ELEMENTS_LIST = (By.CSS_SELECTOR, '.category-cards > div:nth-child(1)')
    FORMS_LIST = (By.CSS_SELECTOR, '.category-cards > div:nth-child(2)')
    ALERTS_LIST = (By.CSS_SELECTOR, '.category-cards > div:nth-child(3)')
    WIDGETS_LIST = (By.CSS_SELECTOR, '.category-cards > div:nth-child(4)')
    INTERACTIONS_LIST = (By.CSS_SELECTOR, '.category-cards > div:nth-child(5)')
    BOOK_STORE_LIST = (By.CSS_SELECTOR, '.category-cards > div:nth-child(6)')

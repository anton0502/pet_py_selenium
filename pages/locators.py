from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class MainPageLocators:
    MAIM_PAGE_LOGO_LINK = (By.CSS_SELECTOR, 'header > a')

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    MAIM_PAGE = (By.CSS_SELECTOR, "#base_page")

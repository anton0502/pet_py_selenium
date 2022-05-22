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


class ElementsPageLocators:
    TEXT_BOX = (By.CSS_SELECTOR, '#item-0')
    FULL_NAME = (By.CSS_SELECTOR, 'input#userName')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#submit')

    CHECK_BOX = (By.CSS_SELECTOR, '#item-1')
    RADIO_BUTTON = (By.CSS_SELECTOR, '#item-2')
    WEB_TABLES = (By.CSS_SELECTOR, '#item-3')
    BUTTONS = (By.CSS_SELECTOR, '#item-4')
    LINKS = (By.CSS_SELECTOR, '#item-5')
    BROKEN_LINKS = (By.CSS_SELECTOR, '#item-6')
    UPLOAD_AND_DOWNLOAD = (By.CSS_SELECTOR, '#item-7')
    DYNAMIC_PROPERTIES = (By.CSS_SELECTOR, '#item-8')

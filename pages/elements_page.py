from pages.base_page import BasePage
from pages.locators import ElementsPageLocators
import allure


class ElementsPage(BasePage):
    def should_open_text_box_tab(self):
        with allure.step('should_open_text_box_tab'):
            self.click(*ElementsPageLocators.TEXT_BOX)
            assert self.correct_url('https://demoqa.com/text-box'), \
                f'The link is wrong or it has changed. Current url - {self.browser.current_url}'

    def should_contain_all_text_box_fields(self):
        self.should_contain_full_name_field()
        self.should_contain_email_field()
        self.should_contain_current_address_field()
        self.should_contain_permanent_address_field()
        self.should_contain_submit_button()

    def should_fill_all_text_box_fields(self):
        self.should_open_text_box_tab()
        self.should_fill_full_name()
        self.should_fill_email()
        self.should_fill_current_address()
        self.should_fill_permanent_address()

    def should_contain_full_name_field(self):
        with allure.step('should_contain_full_name_field'):
            assert self.is_element_present(*ElementsPageLocators.FULL_NAME), f'Field Full Name was not found'

    def should_contain_email_field(self):
        with allure.step('should_contain_email_field'):
            assert self.is_element_present(*ElementsPageLocators.EMAIL_FIELD), f'Field email was not found'

    def should_contain_current_address_field(self):
        with allure.step('should_contain_current_address_field'):
            assert self.is_element_present(*ElementsPageLocators.CURRENT_ADDRESS),\
                f'Field current address was not found'

    def should_contain_permanent_address_field(self):
        with allure.step('should_contain_permanent_address_field'):
            assert self.is_element_present(*ElementsPageLocators.PERMANENT_ADDRESS),\
                f'Field permanent address was not found'

    def should_contain_submit_button(self):
        with allure.step('should_contain_submit_button'):
            assert self.is_element_present(*ElementsPageLocators.SUBMIT_BUTTON), f'Field submit button was not found'

    def should_fill_full_name(self):
        with allure.step('should_fill_full_name'):
            self.write(*ElementsPageLocators.FULL_NAME, 'John Smith')

    def should_fill_email(self):
        with allure.step('should_fill_email'):
            self.write(*ElementsPageLocators.EMAIL_FIELD, 'JohnSmith@gmail.com')

    def should_fill_current_address(self):
        with allure.step('should_fill_current_address'):
            self.write(*ElementsPageLocators.CURRENT_ADDRESS, 'UK, London, 13 Abbey Road')

    def should_fill_permanent_address(self):
        with allure.step('should_fill_permanent_address'):
            self.write(*ElementsPageLocators.PERMANENT_ADDRESS, 'UK, Liverpool, 23 Mathew Street')

    def should_submit_form(self):
        with allure.step('should_submit_form'):
            self.click(*ElementsPageLocators.SUBMIT_BUTTON)

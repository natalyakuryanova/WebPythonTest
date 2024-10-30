import yaml
from BasePage import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send "{word}" to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operate with {locator}')
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word,
                                   description=f"Send {word} to element LOGIN_FIELD")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word,
                                   description=f"Send {word} to element PASS_FIELD")

    def input_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_TITLE_FIELD"], word,
                                   description=f"Send {word} to element POST_TITLE_FIELD")

    def input_description_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION_FIELD"], word,
                                   description=f"Send {word} to element POST_DESCRIPTION_FIELD")

    def input_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT_FIELD"], word,
                                   description=f"Send {word} to element POST_CONTENT_FIELD")

    def enter_your_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME_CONTACT"], word,
                                   description=f"Send {word} to element NAME_CONTACT")

    def enter_your_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL_CONTACT"], word,
                                   description=f"Send {word} to element EMAIL_CONTACT")

    def enter_your_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACT"], word,
                                   description=f"Send {word} to element CONTENT_CONTACT")

    # CLICK BUTTON

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="Click login button")

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_BTN"], description="Click create post button")

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="Click save post button")

    def click_create_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT"], description="Click create contact")

    def click_submit_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="Click submit contact")

    # GET TEXT

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO"])

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    def get_new_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_SEARCH_TITLE_FIELD"])

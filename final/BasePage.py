import logging, yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
address = testdata["address"]

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = address

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except:
            logging.exception('Find element exception')
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found in element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert_field = self.driver.switch_to.alert
            text = alert_field.text
            logging.info(f"We find text {text} in alert")
            return text
        except:
            logging.exception("Exception with alert")
            return None

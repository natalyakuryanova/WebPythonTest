import yaml, time
from PageObject import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata.get('user')
pwd = testdata.get('pwd')
post_title = testdata.get('post_title')
post_description = testdata.get('post_desc')
post_content = testdata.get('post_content')
your_name = testdata.get('your_name')
your_email = testdata.get('your_email')
your_content = testdata.get('your_content')


class TestPos:

    def test_login_pos(self, browser):
        logging.info("Test Positive Login Starting")
        testpage = OperationsHelper(browser)
        testpage.enter_login(name)
        testpage.enter_pass(pwd)
        testpage.click_login_button()
        assert testpage.get_user_text() == f"Hello, {name}"

    def test_add_post(self, browser):
        logging.info("Test 3 Starting")
        testpage = OperationsHelper(browser)
        testpage.click_create_post_button()
        testpage.input_title_post(post_title)
        testpage.input_description_post(post_description)
        testpage.input_content_post(post_content)
        testpage.click_save_post_button()
        time.sleep(2)
        assert testpage.get_new_title_text() == post_title

    def test_contact_us(self, browser):
        logging.info("Test Contact Us Starting")
        testpage = OperationsHelper(browser)
        testpage.click_create_contact()
        testpage.enter_your_name(your_name)
        testpage.enter_your_email(your_email)
        testpage.enter_your_content(your_content)
        testpage.click_submit_contact()
        time.sleep(5)
        assert testpage.get_alert_text() == "Form successfully submitted"


if __name__ == '__main__':
    pass

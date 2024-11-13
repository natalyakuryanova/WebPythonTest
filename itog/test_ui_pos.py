import yaml, time
from PageObject import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata.get('user')
pwd = testdata.get('pwd')


class TestUIPos:

    def test_login_pos(self, browser):
        logging.info("Test Positive Login Starting")
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.enter_login(name)
        testpage.enter_pass(pwd)
        testpage.click_login_button()
        assert testpage.get_user_text() == f"Hello, {name}"

    def test_about(self, browser):
        logging.info('Test Positive About Starting')
        testpage = OperationsHelper(browser)
        testpage.click_about()
        time.sleep(5)
        assert testpage.get_about_text() == ("About Page")
        assert testpage.get_about_property() == "32px"


if __name__ == '__main__':
    pass

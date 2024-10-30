from PageObject import OperationsHelper
import logging
import time


class TestUINeg:
    def test_login_neg(self, browser):
        logging.info('Test Negative Login Starting')
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.enter_login('test')
        testpage.enter_pass('test')
        testpage.click_login_button()
        assert testpage.get_error_text() == '401'
        time.sleep(10)


if __name__ == '__main__':
    pass

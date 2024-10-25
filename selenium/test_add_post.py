from symtable import Class

import time
import yaml
from module import Site

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    name = testdata.get('user')
    passwd = testdata.get('pwd')
    post_title = testdata.get('post_title')
    post_description = testdata.get('post_desc')
    post_content = testdata.get('post_content')

site = Site(testdata['address'])


class TestNeg:
    def test_login(self, x_selector_username, x_selector_password, x_selector_error, btn_selector, er1):
        input1 = site.find_element('xpath', x_selector_username)
        input1.send_keys('test')
        input2 = site.find_element('xpath', x_selector_password)
        input2.send_keys('test')
        btn = site.find_element('css', btn_selector)
        btn.click()
        err_label = site.find_element('xpath', x_selector_error)
        text = err_label.text
        assert text == er1, "Not 401 error"


class TestPos:
    def test_login(self, x_selector_username, x_selector_password, x_selector_hello, btn_selector, hello):
        input1 = site.find_element('xpath', x_selector_username)
        input1.clear()
        input1.send_keys(name)
        input2 = site.find_element('xpath', x_selector_password)
        input2.clear()
        input2.send_keys(passwd)
        btn = site.find_element('css', btn_selector)
        btn.click()
        hello_label = site.find_element('xpath', x_selector_hello)
        text = hello_label.text
        # site.quit()
        assert text == hello, "Don't see hello title"

    def test_add_post(self, create_btn, post_title_input, post_description_input, post_content_input, post_save_btn,
                      post_title_selector):
        # Click + button
        btn = site.find_element('css', create_btn)
        btn.click()
        time.sleep(testdata['wait'])

        # Add post data
        title_input = site.find_element('xpath', post_title_input)
        title_input.send_keys(post_title)
        description_input = site.find_element('xpath', post_description_input)
        description_input.send_keys(post_description)
        content_input = site.find_element('xpath', post_content_input)
        content_input.send_keys(post_content)
        time.sleep(testdata['wait'])

        # Click save post button
        save_btn = (site.find_element('css', post_save_btn))
        save_btn.click()
        time.sleep(testdata['wait'])

        # Check new post presence
        post_title_element = site.find_element('xpath', post_title_selector)
        assert post_title_element.text == post_title, "Can't find new selenium post"

        # Quit browser
        site.quit()

if __name__ == '__main__':
    pass

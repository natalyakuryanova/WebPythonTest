import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

with open("./apidata.yaml") as f:
    apidata = yaml.safe_load(f)


@pytest.fixture(scope='session')
def browser():
    if testdata['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login():
    res = requests.post(testdata["address"] + "gateway/login",
                        data={"username": testdata["user"], "password": testdata["pwd"]})
    print(res)
    return res.json()["token"]


@pytest.fixture()
def testtext1():
    return apidata['search_post_title']


@pytest.fixture()
def post_data():
    return {
        "title": apidata['my_post_title'],
        "description": apidata['my_post_desc'],
        "content": apidata['my_post_content']
    }

import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def x_selector_username():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def x_selector_password():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def x_selector_error():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def btn_selector():
    return 'button'


@pytest.fixture()
def er1():
    return '401'


@pytest.fixture()
def x_selector_hello():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def hello():
    return f'Hello, {testdata["user"]}'


@pytest.fixture()
def create_btn():
    return """#create-btn"""


@pytest.fixture()
def post_title_input():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def post_description_input():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def post_content_input():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def post_save_btn():
    return """button[type="submit"]"""


@pytest.fixture()
def post_title_selector():
    return '//*[@id="app"]/main/div/div[1]/h1'

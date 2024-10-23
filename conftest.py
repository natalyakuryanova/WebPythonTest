import pytest, yaml, requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    res = requests.post(data["address"] + "gateway/login",
                        data={"username": data["user"], "password": data["pwd"]})
    print(res)
    return res.json()["token"]


@pytest.fixture()
def testtext1():
    return "пост5"


@pytest.fixture()
def post_data():
    return {
        "title": "Заголовок моего нового поста",
        "description": "Описание моего нового поста",
        "content": "Содержание моего нового поста"
    }



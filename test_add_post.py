import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

# Search post by title test
def test_search_by_title(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres


# New post creation test
def test_add_my_post(login, post_data):
    header = {"X-Auth-Token": login}
    res = requests.post(data["address"] + "api/posts", headers=header, data=post_data)
    assert res.status_code == 200


# Search post by desc test
def test_search_by_desc(login, post_data):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner": "me"}, headers=header)
    descriptions = [i["description"] for i in res.json()["data"]]
    assert post_data["description"] in descriptions

import logging
import yaml
from BaseApi import api_get, api_post

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
post_url = testdata["address"] + "api/posts"


# Search other post by title test
def test_search_by_title(login, testtext1):
    header = {"X-Auth-Token": login}
    params = '{"owner": "notMe"}'

    logging.info("Test API search by title is starting")
    res = api_get(url=post_url, header=header, params=params)

    assert res is not None
    assert res.status_code == 200

    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres


# New post creation test
def test_add_my_post(login, post_data):
    header = {"X-Auth-Token": login}

    logging.info("Test API create post is starting")
    res = api_post(url=post_url, header=header, data=post_data)

    assert res is not None
    assert res.status_code == 200


# Search my post by desc test
def test_search_my_post_by_desc(login, post_data):
    header = {"X-Auth-Token": login}
    params = '{"owner": "me"}'

    logging.info("Test API search my just created post by desc is starting")
    res = api_get(url=post_url, header=header, params=params)

    assert res is not None
    assert res.status_code == 200

    descriptions = [i["description"] for i in res.json()["data"]]
    assert post_data["description"] in descriptions

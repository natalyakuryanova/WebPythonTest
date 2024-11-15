import logging
import yaml
from PageAPI import ApiOperationsHelper

with open("apidata.yaml") as f:
    apidata = yaml.safe_load(f)
uid = apidata["uid"]

class TestApiPos:
    def test_login(self):
        logging.info("Test API Login (get token) Starting")
        apitestpage = ApiOperationsHelper()
        token = apitestpage.get_token()
        assert token, "Can't login (get token)"

    def test_user(self):
        logging.info("Test API User (get name) Starting")
        apitestpage = ApiOperationsHelper()
        username = apitestpage.get_user(uid)
        assert username == "Наташа", "Can't get user name"

if __name__ == '__main__':
    pass
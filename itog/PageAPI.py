import yaml
from BaseAPI import BaseAPI
import logging
import requests

with open("./apidata.yaml") as f:
    apidata = yaml.safe_load(f)

login_url = apidata["address"] + "gateway/login"
user_url = apidata["address"] + "api/users/profile"


class ApiOperationsHelper(BaseAPI):
    def get_token(self):
        res = requests.post(login_url, data={"username": apidata["user"], "password": apidata["pwd"]})

        if res.status_code == 200:
            token = res.json()['token']
            logging.debug(f'Получен токен пользователя {token}')
            return token
        else:
            logging.error(f'Ошибка авторизации, код ошибки {res.status_code}. Неверные пароль, логин. ')
            return None

    def get_user(self, uid):
        token = self.get_token()
        res = requests.get(url=user_url + f"/{uid}", headers = {'X-Auth-Token': token})

        if res.status_code == 200:
            name = res.json()['firstName']
            logging.debug(f'Получено имя пользователя {name}')
            return name
        else:
            logging.error(f'Kод ошибки {res.status_code}. Неверные пароль, логин.')
            return None

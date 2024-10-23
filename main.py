import requests
import yaml

# created for test purpose only

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def login():
    res = requests.post(data["address"] + "gateway/login",
                        data={"username": data["user"], "password": data["pwd"]})
    return res.json()["token"]


token = login()
print(token)
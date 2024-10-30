import logging
import requests


def api_get(url, params, header):
    try:
        res = requests.get(url=url, params=params, headers=header)
        logging.debug(
            f"GET request to {url} with params: {params} and headers: {header}. Response code: {res.status_code}")
        return res
    except Exception as e:
        logging.error(f"Exception occurred during GET request to {url} with {params}: {e}")
        return None


def api_post(url, data, header):
    try:
        res = requests.post(url=url, headers=header, data=data)
        logging.debug(
            f"POST request to {url} with headers: {header} and data: {data}. Response code: {res.status_code}")
        return res
    except Exception as e:
        logging.error(f"Exception occurred during POST request to {url}: {e}")
        return None

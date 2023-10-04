import json
import requests
import config
from tests_resources.test_data import test_data_staging

class Endpoint:

    BASE_URL = "https://reqres.in"

    @staticmethod
    def post_call(url, json_data):
        return requests.post(url, json_data)

    @staticmethod
    def get_call(url):
        return requests.get(url)
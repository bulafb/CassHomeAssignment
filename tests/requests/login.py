import logging

from tests import api
from tests.payload.user_payload import Login
from tests.api.base import Endpoint
import json


class LoginApi(Endpoint):

    @staticmethod
    def login_call():
        url = LoginApi.get_login_url()
        json_file = open('C:\\Users\\bular\\CassHomeAssignment\\tests_resources\\test_data\\login_payload.json','r')
        json_input = json_file.read()
        json_data = json.loads(json_input)
        logging.info("input request payload is \n\n")
        logging.info(json_data)
        response = Endpoint.post_call(url, json_data)
        return response


    @staticmethod
    def login_call_new():
        url = LoginApi.get_login_url()
        payload = Login.user_login()
        print(payload)
        json_data = json.dumps(payload)
        response = Endpoint.post_call(url, json_data)
        return response


    @staticmethod
    def invalid_login_call():
        url = LoginApi.get_login_url()
        payload = {}
        response = Endpoint.post_call(url, payload)
        return response

    @staticmethod
    def register_call():
        url = LoginApi.get_register_url()
        json_file = open('C:\\Users\\bular\\CassHomeAssignment\\tests_resources\\test_data\\register_payload.json','r')
        json_input = json_file.read()
        json_data = json.loads(json_input)
        response = Endpoint.post_call(url, json_data)
        return response

    @staticmethod
    def invalid_register_call():
        url = LoginApi.get_register_url()
        payload = {}
        response = Endpoint.post_call(url, payload)
        return response


    @staticmethod
    def list_resource_call():
        url = LoginApi.get_list_resource_url()
        response = Endpoint.get_call(url)
        return response


    @staticmethod
    def get_login_url():
        return Endpoint.BASE_URL + api.ENDPOINT_LOGIN_USER

    @staticmethod
    def get_register_url():
        return Endpoint.BASE_URL + api.ENDPOINT_REGISTER_USER

    @staticmethod
    def get_list_resource_url():
        return Endpoint.BASE_URL + api.ENDPOINT_LIST_RESOURCE

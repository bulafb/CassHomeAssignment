import json
import logging
from pytest_bdd import parsers, scenarios, then, when, given
from tests.requests.login import LoginApi
from tests.conftest import response_to_json
from tests.helpers.test_context import TestContext
from tests import api
from tests.api.base import Endpoint


scenarios("loginapi/")

"""Step definitions - Login, Register API , List Resource"""

@given("I post into login API with valid request")
def login_user():
    response = LoginApi.login_call()
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Login request is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_LOGIN_USER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )



@given("I post into login API with empty request")
def invalid_login_user():
    response = LoginApi.invalid_login_call()
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.error_message = response_json ["error"]
    logging.info(
        "The response of Login request is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_LOGIN_USER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )



@given('I post into register API with empty request')
def invalid_register_user():
    response = LoginApi.invalid_register_call()
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.error_message = response_json ["error"]
    logging.info(
        "The response of Login request is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_REGISTER_USER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )


@given("I post into register API with valid request")
def register_user():
    response = LoginApi.register_call()
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Login request is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_REGISTER_USER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )


@given("I do a get list resource")
def list_resource():
    response = LoginApi.list_resource_call()
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.response_data_id =  response_json["data"][0]["id"]
    TestContext.response_data_name = response_json["data"][0]["name"]
    logging.info(
        "The response of Login request is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_LIST_RESOURCE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )


@when(parsers.parse('I see a {status_code} status code returned'))
def status_code(status_code):
    assert TestContext.response_status_code == int(status_code),"status code returned is not as expected"


@then(parsers.parse('I can confirm that {data_id} and {data_name} is returned correctly'))
def list_resource_data(data_id, data_name):
     assert TestContext.response_data_id == int(data_id), "Data id is incorrect"
     assert TestContext.response_data_name == data_name, "Data name is incorrect"


@then(parsers.parse('I see an {error_message}'))
def error_message(error_message):
    assert TestContext.error_message == error_message
import json
import pytest
from json import JSONDecodeError
from requests.exceptions import HTTPError
from pytest_bdd import given, parsers, then, when


def response_to_json(response):
    try:
        response_json = response.json()
    except JSONDecodeError or Exception:
        raise Exception(f"Empty response and the response Status Code is {str(response.status_code)}")
    return response_json


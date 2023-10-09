import json
import logging
from tests.api.base import Endpoint
from tests.helpers import constants
from tests_resources.test_data import test_data_staging


class Login:
    @staticmethod
    def user_login():
        user_email = test_data_staging.login_valid_data.get(constants.EMAIL)
        password = test_data_staging.login_valid_data.get(constants.PASSWORD)
        payload = {
            "email": user_email,
            "password": password
        }
        json_payload = json.dumps(payload)
        logging.info("The request payoad for valid login is "
                     + json_payload
                     )
        return payload

    def register_login():
        user_email = test_data_staging.register_valid_data.get(constants.EMAIL)
        password = test_data_staging.register_valid_data.get(constants.PASSWORD)
        payload = {
            "email": user_email,
            "password": password
        }
        json_payload = json.dumps(payload)
        logging.info("The request payoad for valid register is "
                     + json_payload
                     )
        return payload
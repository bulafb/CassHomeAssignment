from tests_resources.test_data import test_data_staging

class EnvironmentDetails:
    def __init__(self, base_url, test_data):
        self.base_url = base_url
        self.test_data = test_data


STAGING = EnvironmentDetails(base_url="https://reqres.in", test_data=test_data_staging)



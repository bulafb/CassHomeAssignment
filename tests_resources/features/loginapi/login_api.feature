@api_login @regression
Feature: Login API
  As a Cassini user
  I want to login to test API
  so that i get a successful response

@api_login_test
  Scenario Outline: Login to API successful scenario
    Given I post into login API with valid request
    When I see a <status_code_returned> status code returned
    Then A token value is returned

    Examples:
      |status_code_returned|
      |200                 |


 @api_login_invalid
  Scenario Outline: Login to API negative scenario
    Given I post into login API with empty request
    When I see a <status_code_returned> status code returned
    Then I see an <error_message>

    Examples:
      |status_code_returned|error_message             |
      |400                 |Missing email or username |










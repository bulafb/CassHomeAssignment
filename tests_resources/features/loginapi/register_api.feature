@api_login @regression
Feature: Register API
  As a Cassini user
  I want to register to test API
  so that i get a successful response

@api_register_test
  Scenario Outline: Register test API successful scenario
    Given I post into register API with valid request
    When I see a <status_code_returned> status code returned

    Examples:
      |status_code_returned|
      |200                 |


 @api_register_invalid
  Scenario Outline: Register API negative scenario
    Given I post into register API with empty request
    When I see a <status_code_returned> status code returned
    Then I see an <error_message>

    Examples:
      |status_code_returned|error_message             |
      |400                 |Missing email or username |



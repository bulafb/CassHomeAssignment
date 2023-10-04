@list_resource @regression
Feature: List resource
  As a Cassini user
  I want to list resource
  so that i get a successful response

@api_list_resource_test
  Scenario Outline: List resource
    Given I do a get list resource
    Then I see a <status_code_returned> status code returned
    And I can confirm that <data_id> and <data_name> is returned correctly

    Examples:
      |status_code_returned|data_id  |data_name |
      |200                 |1        |cerulean  |


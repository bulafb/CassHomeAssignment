# CassHomeAssignment

# Set Up
This project requires an up-to-date version of Python 3 (Currently using Python 3.11.4)

It also uses pipenv to manage packages.
To set up this project on your local machine:
1. Clone the repo from github https://github.com/bulafb/CassHomeAssignment
2. Run `pipenv install` from the project's root directory.

   # Running Tests

1. Test Execution:
    - Use `pytest` command 
    - Use markers '-m' to filter tests by BDD tags
  
      eg: pytest -m regression
      This will run all the tests

      pytest -m api_login
      This will run tests for login API

import allure
from all_api.api import APITester

@allure.feature('Send Request Feature')
@allure.severity('critical')
@allure.story('Testing the send request functionality')
def test_run_send_request():
    """
    Test for the send request functionality using the AllSports API.
    """
    api_tester = APITester("https://www.allsports.fit")
    result = api_tester.test_send_request()
    print("Result of send request:", result)

@allure.feature('GraphQL Request Feature')
@allure.severity('normal')
@allure.story('Testing the GraphQL request functionality')
def test_run_graphql_request():
    """
    Test for the GraphQL request functionality using the AllSports API.
    """
    api_tester = APITester("https://www.allsports.fit")
    result = api_tester.test_graphql_request()
    print("Result of GraphQL request:", result)

@allure.feature('Custom GraphQL Request Feature')
@allure.severity('critical')
@allure.story('Testing a custom GraphQL request functionality')
def test_run_custom_graphql_request():
    """
    Test for a custom GraphQL request functionality using the AllSports API.
    """
    api_tester_v2 = APITester("https://www.allsports.fit")
    result = api_tester_v2.test_custom_graphql_request()
    print("Result of Custom GraphQL request:", result)

@allure.feature('Another Custom GraphQL Request Feature')
@allure.severity('critical')
@allure.story('Testing another custom GraphQL request functionality')
def test_run_another_custom_graphql_request():
    """
    Test for another custom GraphQL request functionality using the AllSports API.
    """
    api_tester_v3 = APITester("https://www.allsports.fit")
    result = api_tester_v3.test_another_custom_graphql_request()
    print("Result of Another Custom GraphQL request:", result)

@allure.feature('Supplier Request Feature')
@allure.severity('critical')
@allure.story('Testing the supplier request functionality')
def test_run_supplier_request():
    """
    Test for the supplier request functionality using the AllSports API.
    """
    api_tester_v4 = APITester("https://www.allsports.fit")
    result = api_tester_v4.test_supplier_request()
    print("Result of Supplier request:", result)
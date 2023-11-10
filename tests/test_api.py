from all_api.api import APITester


def test_run_send_request():
    api_tester = APITester("https://www.allsports.fit")
    result = api_tester.test_send_request()
    print("Result of send request:", result)

def test_run_graphql_request():
    api_tester = APITester("https://www.allsports.fit")
    result = api_tester.test_graphql_request()
    print("Result of GraphQL request:", result)

def test_run_custom_graphql_request():
    api_tester_v2 = APITester("https://www.allsports.fit")
    result = api_tester_v2.test_custom_graphql_request()
    print("Result of Custom GraphQL request:", result)

def test_run_another_custom_graphql_request():
    api_tester_v3 = APITester("https://www.allsports.fit")
    result = api_tester_v3.test_another_custom_graphql_request()
    print("Result of Another Custom GraphQL request:", result)

def test_run_supplier_request():
    api_tester_v4 = APITester("https://www.allsports.fit")
    result = api_tester_v4.test_supplier_request()
    print("Result of Supplier request:", result)
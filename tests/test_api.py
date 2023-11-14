import allure
import json
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

    try:
        json_result = json.loads(result)
        assert json_result.get("success") == True, "Expected 'success' field to be True in the response, but it is not."
    except json.JSONDecodeError:
        assert False, f"Failed to decode the response as JSON. Response content: {result}"


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

    try:
        json_result = json.loads(result)

        assert "data" in json_result, "Expected 'data' in response JSON, but not found"

        assert "map_markers" in json_result["data"], "Expected 'map_markers' in response JSON, but not found"

        assert isinstance(json_result["data"]["map_markers"], list), "'map_markers' should be a list"

    except json.JSONDecodeError:
        assert False, f"Failed to decode the response as JSON. Response content: {result}"


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

    try:
        # Попробуйте преобразовать строку в JSON
        json_result = json.loads(result)

        # Проверьте, что в ответе есть 'errors', что указывает на неудачное выполнение запроса
        assert "errors" in json_result, "Expected 'errors' in response JSON, but not found"

    except json.JSONDecodeError:
        # Если не удается преобразовать в JSON, считаем тест неудачным
        assert False, f"Failed to decode the response as JSON. Response content: {result}"


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

    try:

        json_result = json.loads(result)

        assert "errors" in json_result, "Expected 'errors' in response JSON, but not found"

    except json.JSONDecodeError:

        assert False, f"Failed to decode the response as JSON. Response content: {result}"


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

    try:

        json_result = json.loads(result)

        assert "data" in json_result, "Expected 'data' in response JSON, but not found"
        assert "supplier" in json_result["data"], "Expected 'supplier' in response JSON, but not found"

        assert "id" in json_result["data"]["supplier"], "Expected 'id' in 'supplier', but not found"
        assert "name" in json_result["data"]["supplier"], "Expected 'name' in 'supplier', but not found"

    except json.JSONDecodeError:

        assert False, f"Failed to decode the response as JSON. Response content: {result}"

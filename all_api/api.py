import requests
import json

class APITester:
    def __init__(self, base_url):
        self.base_url = base_url

    def test_send_request(self):
        url = f"{self.base_url}/send"
        payload = json.dumps({
            "activity": "",
            "city": "test",
            "company": "test",
            "email": "snsanich@gmail.com",
            "employees": "от 10 до 100",
            "name": "Oleg",
            "page": "companies",
            "phone": "35795779879"
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        return response.text

    def test_graphql_request(self):
        url = f"{self.base_url}/graphql"
        payload = {
            "query": """
                {
                  map_markers(
                    general: {
                      language: "by",
                      city: "minsk",
                      country: "by",
                      subscription: "silver",
                      activity: [],
                      tag: []
                    },
                    leftTopPoint: {lat: 53.916593136777024, lng: 27.529234233621136},
                    centerPoint: {lat: 53.9064172603185, lng: 27.546700778726116}
                  ) {
                    lat
                    lng
                    suppliers {
                      id
                      name
                    }
                  }
                }
            """,
            "variables": {}
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.text

    def test_custom_graphql_request(self):
        url = f"{self.base_url}/graphql"
        payload = {
            "query": """
                {
                  custom_map_markers(
                    general: {
                      language: "en",
                      city: "newyork",
                      country: "us",
                      subscription: "gold",
                      activity: ["running"],
                      tag: ["sports"]
                    },
                    leftTopPoint: {lat: 40.7128, lng: -74.0060},
                    centerPoint: {lat: 40.730610, lng: -73.935242}
                  ) {
                    lat
                    lng
                    suppliers {
                      id
                      name
                    }
                  }
                }
            """,
            "variables": {}
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.text

    def test_another_custom_graphql_request(self):
        url = f"{self.base_url}/graphql"
        payload = {
            "query": """
                {
                  another_custom_query(general: {language: "en", city: "newyork"}) {
                    result
                  }
                }
            """,
            "variables": {}
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.text

    def test_supplier_request(self):
        url = f"{self.base_url}/graphql"
        payload = {
            "query": """
                {
                  supplier(id: 330) {
                    id
                    name
                    info
                    rules
                    gallery
                    district
                    condition_list {
                      key
                      value
                    }
                    phone
                    url
                    address
                    lat
                    lng
                    tags
                    mon
                    tue
                    wed
                    thu
                    fri
                    sat
                    sun
                    last_changed_at
                    sh_message
                    sh_url
                    attraction_objects {
                      id
                      list
                      has_copayment
                      copayment
                      levels
                      subscriptions
                    }
                    created_at
                    updated_at
                  }
                }
            """,
            "variables": {}
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.text
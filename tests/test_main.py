import unittest
from fastapi.testclient import TestClient
from app.main import server


class MainTests(unittest.TestCase):
    """
    Tests to characterize and check the routes of the server.
    See https://graphql.org/learn/serving-over-http/
    """
    @classmethod
    def setUpClass(cls):
        cls._client: TestClient = TestClient(server)

    def test_GET_query_hello_OK(self):
        """
        GET requests should specify the GraphQL query as a query string.
        """
        request = '/graphql?query={hello}'
        headers = {'authorization': 'bearer example'}

        response = self._client.get(request, headers=headers)

        self.assertEqual(200, response.status_code)

    def test_POST_json_hello_OK(self):
        """
        POST requests should include a JSON-encoded body with at least a "query" key.
        """
        request = {
            'query': '{ hello }'
        }
        headers = {
            'authorization': 'bearer example',
            'content-type': 'application/json'
        }

        response = self._client.post('/graphql', json=request, headers=headers)

        self.assertEqual(200, response.status_code)

    def test_POST_query_hello_OK(self):
        """
        Typically POST requests have a JSON body, but the spec also supports POSTs
        with a query string.
        """
        request = '/graphql?query={hello}'
        headers = {'authorization': 'bearer example'}

        response = self._client.post(request, headers=headers)

        self.assertEqual(200, response.status_code)

    def test_POST_graphql_hello_OK(self):
        """
        POSTs with the 'application/graphql' content-type have their bodies interpreted
        as GraphQL queries.
        """
        request = """
            query {
                hello
            }
        """
        headers = {
            'authorization': 'bearer example',
            'content-type': 'application/graphql'
        }

        response = self._client.post('/graphql', data=request, headers=headers)

        self.assertEqual(200, response.status_code)

    def test_GET_missing_authorization_header_403(self):
        request = '/graphql?query={hello}'

        response = self._client.get(request)

        self.assertEqual(403, response.status_code)

    def test_POST_missing_authorization_header_403(self):
        request = '/graphql?query={hello}'

        response = self._client.post(request)

        self.assertEqual(403, response.status_code)

    def test_GET_invalid_bearer_token_401(self):
        request = '/graphql?query={hello}'
        headers = {'authorization': 'bearer invalid'}

        response = self._client.get(request, headers=headers)

        self.assertEqual(401, response.status_code)

    def test_POST_invalid_bearer_token_401(self):
        request = '/graphql?query={hello}'
        headers = {'authorization': 'bearer invalid'}

        response = self._client.post(request, headers=headers)

        self.assertEqual(401, response.status_code)


if __name__ == '__main__':
    unittest.main()

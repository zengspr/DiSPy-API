import unittest
from fastapi.testclient import TestClient
from src.main import server


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The type hint is a bit redundant here but I don't get code completion on my
        # IDE without it.
        cls._client: TestClient = TestClient(server)

    def test_EndpointGET_OK(self):
        request = '/api?query={ hello }'

        response = self._client.get(request)

        self.assertEqual(200, response.status_code)

    def test_EndpointPOST_OK(self):
        request = '/api?query={ hello }'

        response = self._client.post(request)

        self.assertEqual(200, response.status_code)

    def test_EndpointPOSTJson_OK(self):
        request = {
            'query': '{ hello }'
        }

        response = self._client.post('/api', json=request)

        self.assertEqual(200, response.status_code)

    def test_EndpointPOSTGraphQL_OK(self):
        request = """
            query {
                hello
            }
        """
        headers = {
            'content-type': 'application/graphql'
        }

        response = self._client.post('/api', data=request, headers=headers)

        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()

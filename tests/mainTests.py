import unittest
from graphene import Schema
from src.main import Query


class MainTests(unittest.TestCase):
    def test_QueryingEndpointHello_ReturnsHelloWorld(self):
        schema = Schema(query=Query)
        request = """{
            hello
        }"""

        response = schema.execute(request)

        self.assertIsNone(response.errors)
        self.assertEqual("Hello World!", response.data['hello'])


if __name__ == '__main__':
    unittest.main()

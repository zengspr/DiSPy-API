import unittest
from graphene import Schema
from src.main import Query


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._schema = Schema(query=Query)

    def test_QueryHelloField_ReturnsHelloWorld(self):
        request = """{
            hello
        }"""

        response = self._schema.execute(request)

        self.assertIsNone(response.errors)
        self.assertEqual("Hello World!", response.data['hello'])

    def test_QueryNotHelloField_ReturnsError(self):
        request = """{
            notHello
        }"""

        response = self._schema.execute(request)

        # Since no schema with field "notHello" is defined on the server
        self.assertIsNotNone(response.errors)

    def test_QueryHelloWithArg_ReturnsError(self):
        request = """{
            hello(name: "spencer")
        }"""

        response = self._schema.execute(request)

        # Since the schema with field "hello" does not have parameters
        self.assertIsNotNone(response.errors)


if __name__ == '__main__':
    unittest.main()

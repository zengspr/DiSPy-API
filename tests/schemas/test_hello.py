import unittest
from graphene.test import Client, Schema
from app.schemas.query import Query


class HelloTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		"""
		Graphene provides Client class that acts as a fake GraphQL client, so you don't
		need to create this testing infrastructure yourself.
		"""
		cls._schema = Schema(query=Query)
		cls._client = Client(cls._schema)

	def test_query_hello_field_returns_hello_world(self):
		request = """
			query {
				hello
			}
		"""

		response = self._client.execute(request)

		self.assertEqual(
			{
				'data': {
					'hello': 'Hello World!'
				}
			}
			, response)


if __name__ == '__main__':
	unittest.main()

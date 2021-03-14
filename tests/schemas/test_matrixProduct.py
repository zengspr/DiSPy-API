import unittest
from graphene.test import Client, Schema
from src.schemas.query import Query


class MatrixProductTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls._schema = Schema(query=Query)
		cls._client = Client(cls._schema)

	def test_QueryMatrixProductField_WithoutArgs_Fails(self):
		request = """
			query {
				matrixOperations {
					product
				}
			}
		"""

		response = self._client.execute(request)

		self.assertFalse('data' in response)
		self.assertTrue('errors' in response)
		self.assertGreaterEqual(len(response['errors']), 1)

	def test_QueryMatrixProductField_WithListOfChars_Fails(self):
		request = """
			query {
				matrixOperations {
					product(first: [["a"]], second: [["b"]])
				}
			}
		"""

		response = self._client.execute(request)

		self.assertFalse('data' in response)
		self.assertTrue('errors' in response)
		self.assertGreaterEqual(len(response['errors']), 1)

	def test_QueryMatrixProductField_WithInvalidMatrices_Fails(self):
		request = """
			query {
				matrixOperations {
					product(first: [[]], second: [[]])
				}
			}
		"""

		# This will produce an stack trace even though the unit test passes.
		response = self._client.execute(request)

		# Here we get back a response because the args are valid, but the service fails, so
		# GraphQL returns a None.
		self.assertIsNone(response['data']['matrixOperations']['product'])
		self.assertTrue('errors' in response)
		self.assertGreaterEqual(len(response['errors']), 1)

	def test_QueryMatrixProductField_WithValidMatrices_OK(self):
		request = """
			query {
				matrixOperations {
					product(first: [[1, 1], [1, 1]], second: [[1, 1], [1, 1]])
				}
			}
		"""

		response = self._client.execute(request)

		self.assertFalse('errors' in response)
		self.assertEqual([[2, 2], [2, 2]], response['data']['matrixOperations']['product'])


if __name__ == '__main__':
	unittest.main()

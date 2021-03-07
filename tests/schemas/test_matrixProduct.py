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
				matrixProduct
			}
		"""

		response = self._client.execute(request)

		self.assertFalse('data' in response)
		self.assertTrue('errors' in response)
		self.assertGreaterEqual(len(response['errors']), 1)

	def test_QueryMatrixProductField_WithListOfChars_Fails(self):
		request = """
			query {
				matrixProduct(first: [["a"]], second: [["b"]])
			}
		"""

		response = self._client.execute(request)

		self.assertFalse('data' in response)
		self.assertTrue('errors' in response)
		self.assertGreaterEqual(len(response['errors']), 1)

	def test_QueryMatrixProductField_WithInvalidMatrices_Fails(self):
		request = """
			query {
				matrixProduct(first: [[]], second: [[]])
			}
		"""

		# This will produce an stack trace even though the unit test passes.
		response = self._client.execute(request)

		# Here we get back a response because the args are valid, but the service fails, so
		# GraphQL returns a None.
		self.assertIsNone(response['data']['matrixProduct'])
		self.assertTrue('errors' in response)
		self.assertGreaterEqual(len(response['errors']), 1)

	def test_QueryMatrixProductField_WithValidMatrices_OK(self):
		request = """
			query {
				matrixProduct(first: [[1, 2], [3, 4]], second: [[2, 0], [1, 2]])
			}
		"""

		response = self._client.execute(request)

		self.assertFalse('errors' in response)
		self.assertEqual([[4, 4], [10, 8]], response['data']['matrixProduct'])


if __name__ == '__main__':
	unittest.main()

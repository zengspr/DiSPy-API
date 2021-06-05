import unittest
from graphene.test import Client, Schema
from app.schemas.query import Query


class DiSPyTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls._schema = Schema(query=Query)
		cls._client = Client(cls._schema)

	def test_dispy_default_args_returns_correct_result(self):
		request = """
					query {
						dispy(perturb: true, numImages: 9) {
							distortionGroup
							possibleIrreps(distortionGroupName: "Cmcm*")
							perturbedPath(irrepNumber: 2857)
						}
					}
				"""

		response = self._client.execute(request)
		print(response)
from graphene import ObjectType, Int, List, Field, Argument
from graphql import GraphQLError

from app.services import numpy_service

import numpy as np

# This variable is defined here so that it's not exposed as a field on the GraphQL type.
matrix = List(List(Int))


class MatrixOperations(ObjectType):
	# Return type followed by args
	product = Field(
		matrix, first=Argument(matrix, required=True), second=Argument(matrix, required=True))

	def resolve_product(
			self, info, first: type(matrix), second: type(matrix)) -> type(matrix):
		"""
		Somehow Graphene.List works as an argument to np.asarray and we can also automatically
		convert from a python list back to a Graphene.List. It also seems like exception messages
		are automatically passed to the GraphQL client in the response.
		"""
		first_matrix = np.asarray(first, dtype=np.int32)
		second_matrix = np.asarray(second, dtype=np.int32)

		try:
			product = numpy_service.matrix_product(first_matrix, second_matrix)
		except ValueError:
			raise GraphQLError('Invalid arguments')

		return product.tolist()
from graphene import ObjectType, String, Int, List, Field, Argument
from graphql import GraphQLError

import numpy as np

from src.integrations import numpyService


class Query(ObjectType):
	"""
	This class represents a GraphQL schema with the structure:
	schema {
		query {
			hello: String!
			matrixProduct(first: [[Int]], second: [[Int]]): [[Int]]
		}
	}

	All of the resolvers for query operations will live in this class.

	TODO:
		- Make each ObjectType in Query into a separate class and import it
	"""

	# hello: String!
	hello = String(required=True)

	def resolve_hello(self, info):
		"""
		Every field has a corresponding resolver that specifies how to respond to a query
		(aka produce a "payload").
		Note that we need to keep the 'info' param even if we don't use it or else we get an exception.
		"""
		return "Hello World!"


	# matrixProduct(...): [[Int!]!]!
	matrix = List(List(Int))
	matrixProduct = Field(
		matrix, first=Argument(matrix, required=True), second=Argument(matrix, required=True))

	def resolve_matrixProduct(
			self, info, first: type(matrix), second: type(matrix)) -> type(matrixProduct):
		"""
		Somehow Graphene.List works as an argument to np.asarray and we can also automatically
		convert from a python list back to a Graphene.List. It also seems like exception messages
		are automatically passed to the GraphQL client in the response.
		"""
		first_np = np.asarray(first, dtype=np.int32)
		second_np = np.asarray(second, dtype=np.int32)

		try:
			product = numpyService.matrixProduct(first_np, second_np)
		except ValueError:
			raise GraphQLError('Invalid arguments')

		return product.tolist()

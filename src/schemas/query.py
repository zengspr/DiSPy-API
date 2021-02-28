from graphene import ObjectType, String


class Query(ObjectType):
	"""
	This class represents a GraphQL schema with the structure:
		type Hello {
			hello: String!
		}

	All the resolvers for query operations will live in this class.
	"""
	hello = String()  # Class attributes are used to represent fields.

	def resolve_hello(self, info):
		"""
		Every field has a corresponding resolver that specifies how to
		respond to a query (aka produce a "payload").
		"""
		return "Hello World!"

from graphene import ObjectType, String, Field

from app.fields.matrix_operations import MatrixOperations


class Query(ObjectType):
	"""
	This class represents the query types in a GraphQL API with the schema:
		query {
			hello: String!
			matrixOperations {
				matrixProduct(first: [[Int]], second: [[Int]]): [[Int]]
			}
			dispy(Path) {
				distortionGroup(IO1, IO2, ...): String
				possibleIrreps(...),
				perturbedPath(...),
			},
		}
	"""
	hello = String(required=True)

	def resolve_hello(self, info):
		"""
		Every field has a corresponding resolver that specifies how to respond to a query
		(aka produce a "payload").
		Note that we need to keep the 'info' param even if we don't use it or else we get an exception.
		"""
		return "Hello World!"

	# This field is an ObjectType instead of a Scalar like 'hello'.
	matrix_operations = Field(MatrixOperations)

	def resolve_matrix_operations(self, info):
		"""
		Resolve to whatever MatrixOperations resolves to.
		TODO: How does this work? Is this the correct semantics?
		"""
		return MatrixOperations()

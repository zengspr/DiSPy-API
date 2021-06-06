from graphene import Boolean, Field, List

from app.fields.matrix_operations import MatrixOperations
from app.fields.dispy import *
from tests.utils.test_utils import get_test_structures


Structures = List(String) # represents a collection of pymatgen Structures

class Query(ObjectType):
	"""
	This class represents the query types in a GraphQL API with the schema:
		query {
			hello: String!
			matrixOperations {
				product(first: [[Int]], second: [[Int]]): [[Int]]
			}
			dispy(perturb: Boolean!, numImages: Int!, structures: [String], ...) {
				distortionGroup(): String
				possibleIrreps(distortionGroupName: String!): String,
				perturbedPath(irrepNumber: Int!): String,
			},
		}
	"""
	hello = String(required=True) # implicitly mounted class attribute
	@staticmethod
	def resolve_hello(parent, info):
		"""
		Every field has a corresponding resolver that specifies how to respond to a query
		(aka produce a "payload").
		Note that we need to keep the 'info' param even if we don't use it or else we get an exception.
		"""
		return "Hello World!"

	# This field is an "compound" type ObjectType instead of a Scalar like 'hello'.
	matrix_operations = Field(MatrixOperations)
	@staticmethod
	def resolve_matrix_operations(parent, info):
		"""
		Resolve to whatever MatrixOperations resolves to.
		TODO: How does this work? Is this the correct semantics?
		"""
		return MatrixOperations()

	# TODO: Reevaluate where to put dispy parameters - top level or somewhere else
	dispy = Field(DiSPy,
				  perturb=Argument(Boolean, required=True),
				  num_images=Argument(Int, required=True),
				  structures=Argument(Structures, default_value=get_test_structures()))
	@staticmethod
	def resolve_dispy(parent, info, perturb: bool, num_images: int, structures: list[dict]):
		# The object being returned here becomes available through 'parent' in
		# the resolvers for subfields of the dispy field.
		return DiSPyRequest(perturb, num_images, structures)

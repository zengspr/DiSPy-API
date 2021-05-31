from graphene import ObjectType, String, Field, Argument, Boolean, Int

from app.fields.matrix_operations import MatrixOperations
from app.fields.dispy import DiSPy
from app.utils.utils import test_images_dir


class Query(ObjectType):
	"""
	This class represents the query types in a GraphQL API with the schema:
		query {
			hello: String!
			matrixOperations {
				product(first: [[Int]], second: [[Int]]): [[Int]]
			}
			dispy(perturb: Boolean!, numImages: Int!, images: String!, ...) {
				distortionGroup(): Path
				possibleIrreps(distortionGroupName: String!): String,
				perturbedPath(irrepNumber: Int!): Path,
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

	"""
	Let's keep all the necessary arguments as parameters in the top level dispy field for now, and 
	reevaluate when we have a better understanding of GraphQL.
	Need to figure out how the initial guess images will be provided to the API.
	"""
	dispy = Field(DiSPy,
				  perturb=Argument(Boolean, required=True),
				  numImages=Argument(Int, required=True),
				  images=Argument(String, default_value=test_images_dir()))
	def resolve_disPy(self, info, perturb: bool, num_images: int, images: str):
		return DiSPy(perturb, num_images, images)

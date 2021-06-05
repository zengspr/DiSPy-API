from graphene import ObjectType, Int, Argument, String

from app.services.dispy_service import *


class DiSPyRequest:
    """
    Used to share per-request IO & input path data among DiSPy resolvers.
    An instance of this class is passed to resolvers as the 'parent' argument.
    """
    def __init__(self, perturb: bool, num_images: int, images: str):
        self.perturb: bool = perturb
        self.num_images: int = num_images
        self.images: str = images # TODO: update this to receive from frontend
        # TODO: set up other fields

        # Setup data needed for subsequent computations
        self.io = get_IO(perturb, num_images, images)
        self.input_path = get_input_path(self.io)


class DiSPy(ObjectType):
    """
    Represents a GraphQL field with the schema:
    dispy(perturb: Boolean!, numImages: Int!, images: String!, ...) {
				distortionGroup(): DiSPyPath
				possibleIrreps(distortionGroupName: String!): String,
				perturbedPath(irrepNumber: Int!): DiSPyPath,
			}

    TODO: Consider making resolvers return a custom DiSPyPath Graphene Scalar object.
    """
    distortionGroup = String()
    @staticmethod
    def resolve_distortionGroup(parent, info) -> dict:
        compute_distortion_group(parent.io, parent.input_path)
        return parent.input_path.as_dict()

    possibleIrreps = String(distortion_group_name=Argument(String, required=True))
    @staticmethod
    def resolve_possibleIrreps(parent, info, distortion_group_name: str) -> str:
        return get_possible_irreps(distortion_group_name)

    perturbedPath = String(irrep_number=Argument(Int, required=True))
    @staticmethod
    def resolve_perturbedPath(parent, info, irrep_number) -> dict:
        perturbed_path = get_perturbed_path(parent.io, parent.input_path, irrep_number)
        return perturbed_path.as_dict()
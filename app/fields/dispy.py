from graphene import ObjectType, Int, Argument, String

from app.services.dispy_service import *


class DiSPyRequest:
    """
    Used to share per-request IO & input path data among DiSPy resolvers.
    An instance of this class is passed to resolvers as the 'parent' argument.

    TODO:
        - update images to receive from frontend instead of test util
        - add other dispy args
    """
    def __init__(self, perturb: bool, num_images: int, structures: list[dict]):
        """
        :param perturb:
        :param num_images:
        :param structures: A list of dicts corresponding to pymatgen Structures
        """
        self.io = get_IO(perturb, num_images)
        self.input_path = get_input_path(structures)


class DiSPy(ObjectType):
    """
    Represents a GraphQL field with the schema:
    dispy(perturb: Boolean!, numImages: Int!, structures: [String], ...) {
				distortionGroup(): String
				possibleIrreps(distortionGroupName: String!): String,
				perturbedPath(irrepNumber: Int!): String,
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
from graphene import ObjectType, Int, Scalar, Field, Argument, String

from app.services.dispy_service import *


class Path(Scalar):
    """
    Represents a DiSPy Path object as a GraphQL scalar type.
    """

    @staticmethod
    def serialize(path: Path) -> dict:
        return path.as_dict()


class DiSPy(ObjectType):
    """
    This class represents a GraphQL field with the schema:
    dispy(perturb: Boolean!, numImages: Int!, images: String!, ...) {
				distortionGroup(): Path
				possibleIrreps(distortionGroupName: String!): String,
				perturbedPath(irrepNumber: Int!): Path,
			}
    """
    def __init__(self, perturb: bool, num_images: int, images: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.perturb: bool = perturb
        self.num_images: int = num_images
        self.images: str = images # TODO: update this to receive from frontend
        # TODO: set up other fields

        # Setup data needed for subsequent computations
        self.io = get_IO(perturb, num_images, images)
        self.input_path = get_input_path(self.io)

    distortionGroup = Field(Path)
    def resolve_distortionGroup(self, info) -> Path:
        compute_distortion_group(self.io, self.input_path)
        return Path.serialize(self.input_path)

    possibleIrreps = Field(String, distortion_group_name=Argument(String, required=True))
    def resolve_possibleIrreps(self, info, distortion_group_name: str) -> str:
        return get_possible_irreps(distortion_group_name)

    perturbedPath = Field(Path, irrep_number=Argument(Int, required=True))
    def resolve_perturbedPath(self, info, irrep_number) -> Path:
        perturbed_path = get_perturbed_path(self.io, self.input_path, irrep_number)
        return Path(perturbed_path)
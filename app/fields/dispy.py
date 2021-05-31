from graphene import ObjectType, Int, Scalar, Field, Argument, String

from app.services.dispy_service import *


class Path(Scalar):
    def __init__(self, path: Path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path

    @staticmethod
    def serialize(self):
        return self.path.as_dict()


class DiSPy(ObjectType):
    """
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
        self.images: str = images # image directory for now
        # other fields

        # setup IO
        self.io = get_IO(perturb, num_images, images)
        self.input_path = get_initial_path(self.io)

    distortionGroup = Field(Path)
    def resolve_distortionGroup(self, info) -> Path:
        compute_distortion_group(self.io, self.input_path)
        # map self.input_path to GraphQL Path object
        return Path(self.input_path)

    # like a lookup table - give name of a symmetry group, get some properties of that group
    possibleIrreps = Field(String, distortion_group_name=Argument(String, required=True))
    def resolve_possibleIrreps(self, info, distortion_group_name: str) -> str:
        return get_possible_irreps(distortion_group_name)

    perturbedPath = Field(Path, irrep_number=Argument(Int, required=True))
    def resolve_perturbedPath(self, info, irrep_number) -> Path:
        perturbed_path = get_perturbed_path(self.io, self.input_path, irrep_number)
        # map to Path
        return Path(perturbed_path)
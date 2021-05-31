from DiSPy.core.io import IO
from DiSPy.core.path import Path

from DiSPy.dg_elements import get_DG
from DiSPy.core.irreps import IrrepTools
from DiSPy.perturb import gen_perturb

"""
image directory - string, req
interpolation - bool
# images - int (odd positive), req
perturb - bool
symmetry tolerance - positive int but defaults to float?
angle tolerance - nonzero float
general tolerance - positive float
vector tolerance - three floats
transition tolerance - three floats
transformation matrix # - positive int, 0 auto, -1 manual
transformation matrix - 3x3 matrix
origin shift - three floats
input format - string
output format - string
irrep # - positive int, req
irrep dimension - positive int
mode coefficients - nonzero float, elements equal to irrep dimension
minimum movement - positive float
perturbation magnitude - positive float

default format VASP-POSCAR
"""

def get_IO(perturb: bool, num_images: int, images: str) -> IO:
    return IO(perturb=perturb, numIm=num_images, image_dir=images)

def get_initial_path(io: IO) -> Path:
     structure_list = io.get_images()
     return Path(structure_list)

def compute_distortion_group(io: IO, input_path: Path) -> None:
    get_DG(input_path, io)

def get_possible_irreps(distortion_group_name: str) -> str:
    return IrrepTools.possible_irreps(distortion_group_name)

def get_perturbed_path(io: IO, input_path: Path, irrep_number: int) -> Path:
    perturbed_images, basis = gen_perturb(input_path, irrep_number, io)
    return Path(perturbed_images)
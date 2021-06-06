from DiSPy.core.io import IO
from DiSPy.core.path import Path

from DiSPy.dg_elements import get_DG
from DiSPy.core.irreps import IrrepTools
from DiSPy.perturb import gen_perturb

from pymatgen.core import Structure

"""
This service is responsible for integrating DiSPy to the API. 
"""

def get_IO(perturb: bool, num_images: int) -> IO:
	"""
	Returns an IO object that initializes data based on the parameters which are needed for later computations.
	"""
	return IO(perturb=perturb, numIm=num_images)

def get_input_path(structures: list[dict]) -> Path:
	"""
	Returns an input path that is needed for subsequent distortion group and perturbed path computations.
	"""
	return Path([Structure.from_dict(structure) for structure in structures])

def compute_distortion_group(io: IO, input_path: Path) -> None:
	"""
	Returns a distortion group given an IO object and input path.
	"""
	get_DG(input_path, io)

def get_possible_irreps(distortion_group_name: str) -> str:
	"""
	Returns possible irreducible representations associated with the given distortion group e.g. Cmcm*.
	"""
	# like a lookup table - give name of a symmetry group, get some properties of that group
	return IrrepTools.possible_irreps(distortion_group_name)

def get_perturbed_path(io: IO, input_path: Path, irrep_number: int) -> Path:
	"""
	Returns a perturbed path given an input path and an irrep number associated with a material e.g. 2857.
	"""
	perturbed_images, basis = gen_perturb(input_path, irrep_number, io)
	return Path(perturbed_images)
from pathlib import Path
from pymatgen.core import Structure


def test_images_dir() -> Path:
	"""
	Returns the filesystem path corresponding to the location of test VASP images.
	DiSPy-API (root) -> tests -> test_images
	"""
	return Path(__file__).parent.parent.parent / "tests/test_images"

def get_test_structures() -> list[dict]:
	"""
	Returns a collection of pymatgen Structure objects for test purposes.
	"""
	test_images = [str(image_path) for image_path in test_images_dir().glob('*.vasp')]
	return [Structure.from_file(test_image).as_dict() for test_image in test_images]

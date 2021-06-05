from pathlib import Path


def test_images_dir() -> Path:
	"""
	Returns the filesystem path corresponding to the location of test VASP images.
	DiSPy-API (root) -> tests -> test_images
	"""
	return Path(__file__).parent.parent.parent / "tests/test_images"
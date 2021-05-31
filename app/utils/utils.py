from pathlib import Path

# Temporary helper to get files from test_images.
# utils -> app -> DiSPy-API (root)
def test_images_dir() -> Path:
	return Path(__file__).parent.parent.parent / "tests/test_images"
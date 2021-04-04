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

"""
def dispy(dispy params):
	dispy_result = call Dispy(params)
	return dispy_result
"""
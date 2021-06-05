import numpy as np


"""
A "service" represents a third-party integration into the API server.
In this example, the third-party is the NumPy library.

When the GraphQL endpoint receives a request, it forwards it to a service which
is responsible for producing the result.

My current thoughts are that services should not know about GraphQL. Accordingly,
the field resolver is responsible for converting raw GraphQL inputs into the formats expected by the service
and converting the output type of the service into the format expected by the GraphQL client.

In this NumPy example, the resolver method 'resolve_matrix_operations' converts the GraphQL query into 
the np array_like type and converts array_like into the 'matrix' GraphQL scalar type defined in 'MatrixOperations'. 
"""

def matrix_product(first: np.ndarray, second: np.ndarray) -> np.ndarray:
	return np.matmul(first, second)

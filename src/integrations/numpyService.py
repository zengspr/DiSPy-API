import numpy as np


"""
A "service" represents a third-party integration into the API server.
In this example, the service is the NumPy library.

When the GraphQL endpoint receives a request, it forwards it to a service which
is responsible for computing the result.

My current thoughts are that services should not know about GraphQL at all.
Accordingly:
	- The endpoint (e.g. class Query) is responsible for converting raw GraphQL
	inputs into the format expected by the service.
	- The endpoint is responsible for converting the raw output of the service into
	the format expected by the GraphQL client.

In this NumPy example, this means that Query attempts to parse the GraphQL query into
np array_like types and attempts to parse array_like into the custom MatrixProduct GraphQL
scalar. This also means that the MatrixProduct scalar is defined outside of the service class.

Ideally, services should "live by themselves" so that they can be scaled independently of
other services and the internal GraphQL server(s).
"""


def matrixProduct(first: np.ndarray, second: np.ndarray) -> np.ndarray:
	return np.matmul(first, second)


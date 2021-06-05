from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

"""
Provides simple bearer token authorization for the server.
"""

bearer_auth = HTTPBearer()
AUTH_TOKEN: str = "example"  # TODO: Provide via environment variable


async def verify_token(token: HTTPAuthorizationCredentials = Depends(bearer_auth)):
	"""
	This method can be used in the 'dependencies' parameter in path operations to enforce
	bearer token authentication on requests hitting the given path.

	:raises HTTPException: 401 if the request token does not match, 403 if the request is malformed.
	"""
	if token.credentials != AUTH_TOKEN:
		raise HTTPException(401, "Invalid bearer token")

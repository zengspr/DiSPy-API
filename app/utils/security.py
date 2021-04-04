from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

"""
Provides simple bearer token authorization for the server.
"""

bearer_auth = HTTPBearer()
AUTH_TOKEN: str = "example"  # TODO: Provide via environment variable


# HTTPBearer class returns 403 if request authorization is malformed (no authorization
# header or missing 'bearer').
async def verify_token(token: HTTPAuthorizationCredentials = Depends(bearer_auth)):
	if token.credentials != AUTH_TOKEN:
		raise HTTPException(401, "Invalid bearer token")

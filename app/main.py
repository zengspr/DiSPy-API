import uvicorn
from fastapi import FastAPI

from app.routes import graphql

"""
Starts the server. All the server-related configuration (middleware, URLs, etc.) is set up here.
"""

server = FastAPI()

server.include_router(graphql.router)


@server.get("/")
def info():
	return "DiSPy-API"


if __name__ == "__main__":
	"""
	Going to http://localhost:8000/explore in a browser opens an interactive tool to execute 
	GraphQL queries on this server.
	"""
	uvicorn.run(server, host="localhost", port=8000)

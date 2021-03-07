import uvicorn
from fastapi import FastAPI
from graphene import Schema
from starlette.graphql import GraphQLApp
from src.schemas.query import Query
from src.routes import graphql


"""
This is the entry point of the application. All the server-related configuration
(middleware, URLs, etc.) is set up here.
"""

server = FastAPI()

# TODO: Fix this, routes don't work.
#server.include_router(graphql.router)

server.add_route('/api', GraphQLApp(schema=Schema(query=Query)))


@server.get("/")
def info():
	return "DiSPy-API"


if __name__ == "__main__":
	"""
	Going to http://localhost:8000/api opens an interactive tool to execute 
	GraphQL queries on this server.
	"""
	uvicorn.run(server, host="localhost", port=8000)

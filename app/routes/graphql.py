from fastapi import APIRouter, Depends
from graphene import Schema
from starlette.graphql import GraphQLApp, Request

from app.schemas.query import Query
from app.utils.security import verify_token

router = APIRouter()

graphql_app = GraphQLApp(schema=Schema(query=Query))


# See tests.test_main.py for characterizing structure of HTTP requests to the GraphQL endpoint.
@router.get('/graphql', dependencies=[Depends(verify_token)])
async def graphql_endpoint_GET(request: Request):
	# Use starlette Request, not fastapi Request
	return await graphql_app.handle_graphql(request=request)


@router.post('/graphql', dependencies=[Depends(verify_token)])
async def graphql_endpoint_POST(request: Request):
	return await graphql_app.handle_graphql(request=request)


# TODO: Turn off GraphIQL in production.
@router.get('/explore')
async def graphql_explorer(request: Request):
	return await graphql_app.handle_graphql(request=request)


@router.post('/explore')
async def graphql_explorer(request: Request):
	return await graphql_app.handle_graphql(request=request)

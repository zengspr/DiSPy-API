from fastapi import APIRouter
from graphene import Schema
from starlette.graphql import GraphQLApp, Request

from src.schemas.query import Query

router = APIRouter()

graphql_app = GraphQLApp(schema=Schema(query=Query))


# See tests.test_main.py for characterizing structure of HTTP requests to the GraphQL endpoint.
@router.get('/graphql')
async def graphQLEndpointGET(request: Request):
	# NB: Use starlette Request, not fastapi Request
	return await graphql_app.handle_graphql(request=request)


@router.post('/graphql')
async def graphQLEndpointPOST(request: Request):
	return await graphql_app.handle_graphql(request=request)

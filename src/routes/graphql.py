from fastapi import APIRouter
from graphene import Schema
from starlette.graphql import GraphQLApp

from src.schemas.query import Query

router = APIRouter()


@router.api_route('/api', methods=["GET", "POST"])
def graphQLEndpoint():
	return GraphQLApp(schema=Schema(query=Query))

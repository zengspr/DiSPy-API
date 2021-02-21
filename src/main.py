import uvicorn
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello World!"


server = FastAPI()
server.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))


if __name__ == "__main__":
    # Opens an interactive tool to execute GraphQL queries on this server
    uvicorn.run(server, host="localhost", port=8000)

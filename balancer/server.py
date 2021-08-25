from sanic import (
    HTTPResponse,
    Request,
    Sanic,
)

app = Sanic("redir-balancer")


@app.get("/")
async def process_redir(request: Request) -> HTTPResponse:
    pass

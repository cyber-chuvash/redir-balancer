from asyncio import AbstractEventLoop

from sanic import (
    HTTPResponse,
    Request,
    Sanic,
    text,
)
from sanic.response import redirect

from balancer.cdn_url_builder import CDNURLBuilder
from balancer.redirect_decider import (
    AbstractRedirectDecider,
    RatioRedirectDecider,
    RedirectDecision,
)

app = Sanic("redir-balancer")


@app.before_server_start
async def setup_app(app_: Sanic, _loop: AbstractEventLoop) -> None:
    app_.ctx.redirect_decider = RatioRedirectDecider(cdn_request_ratio=1)
    app_.ctx.cdn_url_builder = CDNURLBuilder(cdn_host='cdn.test')


@app.get("/")
async def process_redir(request: Request) -> HTTPResponse:
    video_url = request.args.get('video')
    if video_url is None:
        return text('query parameter missing: "video"', status=400)

    redirect_decider: AbstractRedirectDecider = request.app.ctx.redirect_decider
    cdn_url_builder: CDNURLBuilder = request.app.ctx.cdn_url_builder

    if redirect_decider.decide_redirect(request) is RedirectDecision.CDN:
        cdn_url = cdn_url_builder.make_cdn_url(video_url)
        return redirect(cdn_url, status=302)
    else:
        return redirect(video_url, status=302)

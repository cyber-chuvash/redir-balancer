from typing import cast

import pytest
from sanic import Request

from balancer.redirect_decider import (
    RatioRedirectDecider,
    RedirectDecision,
)


_DUMMY_REQUEST: Request = cast(Request, object())


@pytest.mark.parametrize(
    'ratio',
    (4, 9, 23, 1, 0)
)
def test_ratio_redirect_decider(ratio: int) -> None:
    decider = RatioRedirectDecider(cdn_request_ratio=ratio)
    expected_decisions = (RedirectDecision.CDN,) * ratio + (RedirectDecision.ORIGIN,)

    for exp_decision in expected_decisions * 2 + (RedirectDecision.CDN,) * ratio:
        assert decider.decide_redirect(_DUMMY_REQUEST) is exp_decision
        print(f'Decided: {exp_decision.name}')

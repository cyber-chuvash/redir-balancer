from abc import (
    ABC,
    abstractmethod,
)
from enum import (
    Enum,
    auto,
)

from sanic import Request


class RedirectDecision(Enum):
    ORIGIN = auto()
    CDN = auto()


class AbstractRedirectDecider(ABC):
    @abstractmethod
    def decide_redirect(self, request: Request) -> RedirectDecision: ...


class RatioRedirectDecider(AbstractRedirectDecider):
    def __init__(self, *, cdn_redirect_ratio: int = 9) -> None:
        """
        :param cdn_redirect_ratio: How many CDN redirects to make before making 1 origin redirect
        """
        self._cdn_redirect_ratio = cdn_redirect_ratio
        self._counter = 0

    def decide_redirect(self, request: Request) -> RedirectDecision:
        self._counter += 1
        if self._counter > self._cdn_redirect_ratio:
            self._counter = 0
            return RedirectDecision.ORIGIN
        else:
            return RedirectDecision.CDN

from typing import Optional
from urllib.parse import urlparse


class CDNURLBuilder:
    def __init__(self, *, cdn_host: str) -> None:
        self._cdn_host = cdn_host

    def make_cdn_url(self, origin_url: str) -> str:
        parsed_url = urlparse(origin_url)

        server: Optional[str] = parsed_url.hostname and parsed_url.hostname.split('.', 1)[0]
        location: str = parsed_url.path.lstrip('/')

        if not (server and location):
            raise ValueError(f'cannot find hostname or path in url: {origin_url}')

        return f'http://{self._cdn_host}/{server}/{location}'

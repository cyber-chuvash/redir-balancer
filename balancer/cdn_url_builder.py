from urllib.parse import urlparse


class CDNURLBuilder:
    def __init__(self, *, cdn_host: str) -> None:
        self._cdn_host = cdn_host

    def make_cdn_url(self, origin_url: str) -> str:
        parsed_url = urlparse(origin_url)
        if None in (parsed_url.hostname, parsed_url.path):
            raise ValueError(f'cannot find hostname or path in url: {origin_url}')
        server = parsed_url.hostname.split('.', 1)[0]
        location = parsed_url.path.lstrip('/')

        return f'http://{self._cdn_host}/{server}/{location}'

import pytest

from balancer.cdn_url_builder import CDNURLBuilder


@pytest.mark.parametrize(
    ['origin_url', 'exp_cdn_url'],
    (
        ('http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8',
         'http://cdn.test/s1/video/1488/xcg2djHckad.m3u8'),
        ('http://s2.origin-cluster/video/5423/test34289laala.m3u8',
         'http://cdn.test/s2/video/5423/test34289laala.m3u8'),

        ('http://s2.origin-cluster//video/5423/test34289laala.m3u8',        # double slash //
         'http://cdn.test/s2/video/5423/test34289laala.m3u8'),              # single slash /

        ('http://s2.origin-cluster/video/5423/%7Etest34289.m3u8',           # percent-encoded char (RFC 3986 s. 2.1)
         'http://cdn.test/s2/video/5423/%7Etest34289.m3u8'),
    )
)
def test_cdn_url_builder(origin_url: str, exp_cdn_url: str) -> None:
    url_builder = CDNURLBuilder(cdn_host='cdn.test')
    assert url_builder.make_cdn_url(origin_url) == exp_cdn_url

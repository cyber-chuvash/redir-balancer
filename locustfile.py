from locust import task
from locust.contrib.fasthttp import FastHttpUser


class BalancerUser(FastHttpUser):
    @task
    def get_redir(self):
        self.client.get(
            "/?video=http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8",
            allow_redirects=False
        )

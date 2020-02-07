#-*- coding:utf-8 -*-
import requests

tmp_dict = dict()

class State():
    """
    인터페이스
    """
    def handle(self):
        raise NotImplementedError


class RedisCache(State):
    """
    레디스 캐시 실제 작업
    """
    @classmethod
    def cache(self, url):
        tmp_dict[url] = requests.get(url).text

    @classmethod
    def handle(self, url):
        print("-------------------" + url + "-------------------" )
        print(tmp_dict[url])


class ProxyRedis(State):
    """
    프록시 클래스
    """
    def __init__(self, url):
        self.url = url

    def handle(self):
        if(self.url not in tmp_dict):
            redis_cache = RedisCache.cache(self.url)
        return RedisCache.handle(self.url)


if __name__ == "__main__":
    client1 = ProxyRedis("http://www.09women.com/")
    client1.handle()
    client2 = ProxyRedis("http://www.09women.com/")
    client2.handle()
    client3 = ProxyRedis("http://www.906studio.co.kr/")
    client3.handle()

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
    def __init__(self, url):
        self.url = url
        self.cache()

    def cache(self):
        tmp_dict[self.url] = requests.get(self.url).text

    def handle(self, url):
        print(tmp_dict[url])


class ProxyRedis(State):
    """
    프록시 클래스
    """
    def __init__(self, url):
        self.url = url


    def handle(self):
        if(self.url not in tmp_dict):
            redis_cache = RedisCache(self.url)
        return redis_cache.handle(self.url)


def main():
    client1 = ProxyRedis("https://python.bakyeono.net/chapter-3-4.html")
    client1.handle()
    client2 = ProxyRedis("https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9D%EC%8B%9C_%ED%8C%A8%ED%84%B4")
    client2.handle()
    client3 = ProxyRedis("https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9D%EC%8B%9C_%ED%8C%A8%ED%84%B4")
    client3.handle()
    print(tmp_dict)


if __name__ == "__main__":
    main()
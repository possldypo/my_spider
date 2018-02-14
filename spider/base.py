# coding=utf-8
import requests
import cookielib
import time


class Base(object):

    cookie = cookielib.CookieJar()

    session = requests.Session()

    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        #
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    proxy = {}

    def http_client(self, url, data=None, proxy=None, header=None, method="get", stop=0):
        if not proxy:
            proxy = self.proxy
        if not header:
            header = self.header
        if method == "get":
            response = self.session.get(url, data=data, proxies=proxy, headers=header)
        else:
            response = self.session.post(url, data=data, proxies=proxy, headers=header)
        print("time sleep %d" % stop)
        time.sleep(stop)
        return response.content

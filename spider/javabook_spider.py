# coding=utf-8
import requests

from data_source import Mysql
from spider.base import Base
from entity.javaBook import JavaBook
from bs4 import BeautifulSoup


class JavaBookSpider(Base):

    java_base_list_url = "http://www.java1234.com/a/javabook/javabase/list_65_%d.html"

    def __init__(self):
        self.header.update({"Host": "www.java1234.com"})
        self.conn = Mysql()

    def start(self):
        for page in range(1, self.get_page() + 1):
            list_html = self.http_client(self.java_base_list_url % page, stop=0.3)

    def get_page(self):
        page = int(BeautifulSoup(self.http_client(self.java_base_list_url % 1), "html5lib").find("span", attrs={"class": "pageinfo"}).find("strong").text)
        print "page = [%d]" % page
        return page

    def get_url(self, page_html):
        return ["http://www.java1234.com%s" % tag_a["href"] for tag_a in BeautifulSoup(page_html, "html5lib").find("div", attrs={"class": "listbox"}).find_all("a")]

    def parse_detail(self, detail_url):
        java_book = JavaBook()
        detail_html = self.http_client(detail_url)
        soup = BeautifulSoup(detail_html, "html5lib")
        main_div = soup.find("div", attrs={"class": "viewbox"})
        java_book.title = main_div.find("div", attrs={"class": "title"}).text
        resource_content = soup.find("div", attrs={"class": "viewbox"}).find("div", attrs={"class": "content"}).find_all("tr")[1].find_all("span")[2]


if __name__ == "__main__":
    JavaBookSpider().get_page()

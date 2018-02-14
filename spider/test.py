# coding=utf-8
import os

from bs4 import BeautifulSoup


def create_sequence_number(number, length=5):
    number = "0%s" % str(number)
    if len(number) < length:
        return create_sequence_number(number)
    return "No.%s" % number


def folder_exist(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)


def test():
    html = open("test.html").read()
    soup = BeautifulSoup(html, "html5lib")
    print soup


if __name__ == "__main__":
    test()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# Basic BeautifulSoup

def page(url):
    source_code = requests.get(url)     # requests data
    plain_text = source_code.text       # data to text
    soup = BeautifulSoup(plain_text)    # text to soup
    a = soup.findAll("a", {"class": "nbg"})
    print(a)

    print(plain_text)    # print requests page code

    # print(source.content)
    print("done")

page("https://movie.douban.com/tag/%E7%BE%8E%E5%9B%BD?start=60&type=T")
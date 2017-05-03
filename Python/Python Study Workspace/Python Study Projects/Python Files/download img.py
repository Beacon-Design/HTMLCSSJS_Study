#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python download\ img.py

import random
import urllib.request

def download_img(url):

    # name = random.randrange(1, 100)
    # full_name = str(name) + ".jpg"

    full_name = "downloadimg.jpg"
    urllib.request.urlretrieve(url, full_name)


boat = "https://imgsa.baidu.com/baike/w%3D268/sign=a80791caa68b87d65042ac193f092860/54fbb2fb43166d225451366f412309f79052d222.jpg"
download_img(boat)
print("down img Done")
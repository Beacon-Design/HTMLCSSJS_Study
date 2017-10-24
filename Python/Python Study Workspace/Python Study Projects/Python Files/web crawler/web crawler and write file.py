#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# douban page 20 a page
import requests
from bs4 import BeautifulSoup

def console_print(max_pages):
    page = 0
    print("\nBegin!!!\n")
    while page <= max_pages:
        url = "https://movie.douban.com/tag/%E7%BE%8E%E5%9B%BD?start=" + str(page) + "&type=T"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'nbg'}):
            href = "" + link.get("href")
            title = link.get("title")
            print(href)
            print(title)
            print(link)
        page += 20
    print("\nDone!!!")




def write_file(max_pages):
    page = 0
    fw = open("web crawler and write file.txt", "w")    # creat a file
    fw.write("Begin!!!\n\n")                                # write a file
    while page <= max_pages:
        url = "https://movie.douban.com/tag/%E7%BE%8E%E5%9B%BD?start=" + str(page) + "&type=T"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'nbg'}):
            href = "" + link.get("href")
            title = link.get("title")
            fw.write(href + "\n")
            fw.write(title + "\n\n")
        page += 20
    fw.write("\n\nDone!!!")
    fw.close()



console_print(20)
write_file(20)

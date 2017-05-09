#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# douban page 20 a page
import requests
from bs4 import BeautifulSoup

# def console_print(max_pages):
#     page = 0
#     print("\nBegin!!!\n")
#     while page <= max_pages:
#         url = "https://movie.douban.com/tag/%E7%BE%8E%E5%9B%BD?start=" + str(page) + "&type=T"
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#         for link in soup.findAll('a', {'class': 'nbg'}):
#
#
#             href_link = link.get("href")
#
#             page_inside(href_link)
#
#             # title = link.get("title")
#             # print(href_link)
#             # print(title)
#             # print(link)
#         page += 20
#
#     print("\nDone!!!")

def messageHistoryLinks(messageHistory_url):
    source_code = requests.get(messageHistory_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link_content in soup.findAll('h4', {'class': 'weui_media_title'}):
        link_text = link_content.get_text()                      # get text in ankor a
        print(link_text)
    print('Done!')
    print(soup.prettify())

url = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzIxMjEzODA5Mw==&scene=124#wechat_redirect'
messageHistoryLinks(url)


# def write_file(max_pages):
#     page = 0
#     fw = open("web crawler and write file.txt", "w")    # creat a file
#     fw.write("Begin!!!\n\n")                                # write a file
#     while page <= max_pages:
#         url = "https://movie.douban.com/tag/%E7%BE%8E%E5%9B%BD?start=" + str(page) + "&type=T"
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, "html.parser")
#         for link in soup.findAll('a', {'class': 'nbg'}):
#             href = "" + link.get("href")
#             title = link.get("title")
#             fw.write(href + "\n")
#             fw.write(title + "\n\n")
#         page += 20
#     fw.write("\n\nDone!!!")
#     fw.close()

# console_print(20)
# write_file(20)

#!/usr/bin/env python3
#coding:utf-8

import movie
import fresh_tomatoes

test01 = movie.Movieclass("Toy",
                       "a good story",
                       "http://123",
                       "https://www.baidu.com")
test02 = movie.Movieclass("02",
                          "this is test 02",
                          "http://cn.bing.com/images/search?view=detailV2&ccid=eIBxq60g&id=CC6F19E083A5ADB257713540175F125C94CB0CAF&thid=OIP.eIBxq60gDYXSUEF4oLy9GwEsC7&q=%E8%B4%9D%E5%A3%B3%E6%91%84%E5%BD%B1&simid=608040441507744036&selectedIndex=0",
                          "http://cn.bing.com/")
test03 = movie.Movieclass("03",
                          "this is test 03",
                          "http://cn.bing.com/images/search?view=detailV2&ccid=9GhVh7n%2f&id=5EB68EF4C9BF300878C82271916138B0F2318CBB&thid=OIP.9GhVh7n_rAGbcwzFpRGVPwE8DF&q=%E8%B7%91%E8%BD%A6%E5%A3%81%E7%BA%B8&simid=608042683469922830&selectedIndex=1&ajaxhist=0",
                          "https://www.yandex.com/")
# print(toy_story.title)
# toy_story.show_trailer()        # instance method

movies = [test01, test02, test03 ]
fresh_tomatoes.open_movies_page(movies)
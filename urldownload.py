#!/usr/env/bin python3
# -*- coding:utf-8 -*-

import urllib.request, urllib.error, http.cookiejar

# 创建cookie容器
cj = http.cookiejar.CookieJar()

# 创建一个opener
opener = urllib.request.build_opener(urllib2.HTTPCookieProcessor(cj))

# 给urllib2安装opener
urllib.request.install_opener(opener)

# 创建Request对象
request = urllib.request.Request(url)

# 添加数据
request.add_data('a', '1')
# 添加http的header
request.add_header('User-Agent', 'Mozilla/5.0')

# 发送请求获取结果
response = urllib.request.urlopen(request)

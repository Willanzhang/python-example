#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import urllib2

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]

user_agent = random.choice(ua_list);

request = urllib2.Request(url);

response = request.urlopen(request)


# #也可以通过调用Request.add_header() 添加/修改一个特定的header
# request.add_header("Connection", "keep-alive")

# # 也可以通过调用Request.get_header()来查看header信息
# request.get_header(header_name="Connection")
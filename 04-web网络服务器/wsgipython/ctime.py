# coding:utf-8

import time

def application(env, startResponse):
    status = "200 ok"
    headers = [
      ("Content-Type", "text/plain"),
      ("Server", "My Server"),
    ]
    startResponse(status, headers)
    return time.ctime()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : scanredis.py
@Author : Chico Malo
@Time : 2025/9/17 19:09  
@脚本说明 : 
"""


import concurrent.futures
import redis


def scan_redis(host="127.0.0.1", port=6379, password="", timeout=5):
    try:
        redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            db=10,
            socket_timeout=3,
            socket_connect_timeout=timeout
        )
        if redis_client.ping():
            print(f"[+] {host}:{port} 存在Redis弱口令 -> {password}")
    except Exception as e:
        f"redis弱口令漏洞扫描出错: {e}"
        pass

def redisMain(host,port,passwds,threadsNum=1000):
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadsNum) as executor:
        for passwd in passwds:
            passwd = passwd.strip()
            executor.submit(scan_redis, host=host, port=port, password=passwd)

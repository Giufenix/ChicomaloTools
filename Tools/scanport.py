#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : scanport.py
@Author : Chico Malo
@Time : 2025/9/17 19:09  
@脚本说明 : 
"""


import concurrent.futures
import socket


def scanPort(host, startPort,interval):
    for port in range(startPort, startPort + interval):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(0.1)
            result = tcp.connect_ex((host, port))
            if result == 0:
                print(f"[+] {host}:{port} 端口开启")
            tcp.close()
        except Exception as e:
            f"端口扫描异常: {e}"
            pass


def portMain(host, interval=10, threadsNum=100):
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadsNum) as executor:
        for i in range(1,65535,interval):
            executor.submit(scanPort, host, i, interval)

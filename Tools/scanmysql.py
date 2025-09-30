#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : scanmysql.py
@Author : Chico Malo
@Time : 2025/9/17 19:09  
@脚本说明 : 
"""


import concurrent.futures
import pymysql

def scanMysql(host="127.0.0.1", port=3306, user="root", password="", connect_timeout=1):
    try:
        pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            connect_timeout=connect_timeout,
            database="information_schema",
            charset="utf8",
            autocommit=True,
        )
        print(f"[+] {host}:{port} 存在MySQL数据库弱口令 -> {user} / {password}")
    except Exception as e:
        f"数据库弱口令漏洞扫描出错：{e}"
        pass

def mysqlMain(host,port,users,passwds,threadsNum=1000):
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadsNum) as executor:
        for user in users:
            user = user.strip()
            for passwd in passwds:
                passwd = passwd.strip()
                executor.submit(scanMysql, host=host,port= port, user=user, password=passwd)

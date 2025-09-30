#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : scanssh.py
@Author : Chico Malo
@Time : 2025/9/17 19:09  
@脚本说明 : 
"""


import concurrent.futures
import warnings
import paramiko


warnings.filterwarnings("ignore")
def ssh_connect(host, port=22, username="root", password="root"):
    try:
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        ssh_client = paramiko.SSHClient()
        if ssh_client:
            print(f"[+] SSH连接成功: {username} / {password}")
            ssh_client.close()
            transport.close()
            return True
        else:
            print(f"[-] SSH 连接失败: {username} / {password}")
            ssh_client.close()
            transport.close()
            return False
    except Exception as e:
        f"ssh弱口令漏洞扫描出错: {e}"
        pass

def sshMain(host,port,users,passwds,threadsNum=1000):
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadsNum) as executor:
        for user in users:
            user = user.strip()
            for passwd in passwds:
                passwd = passwd.strip()
                executor.submit(ssh_connect, host=host, port=port, username=user, password=passwd)
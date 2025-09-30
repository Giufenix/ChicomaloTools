#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : getTools.py
@Author : Chico Malo
@Time : 2025/9/17 19:05  
@脚本说明 : 
"""


from Tools.scanip import ipMain
from Tools.scanssh import sshMain
from Tools.scanport import portMain
from Tools.scanmysql import mysqlMain
from Tools.scanredis import redisMain
from Tools.scansubdomains import subdomainsMain




def useTools(operate):
    if operate['toolName'] == "ip":
        ipMain(nodeIP = operate['data']['nodeIP'], netmask = operate['data']['netmask'],
                threadsNum = operate['data']['threadsNum'])

    elif operate['toolName'] == "port":
        portMain(host = operate['data']['host'], interval = operate['data']['interval'],
                threadsNum = operate['data']['threadsNum'])

    elif operate['toolName'] == "mysql":
        mysqlMain(host = operate['data']['host'], port = operate['data']['port'],
                users = operate['data']['username'], passwds = operate['data']['password'],
                threadsNum = operate['data']['threadsNum'])

    elif operate['toolName'] == "redis":
        redisMain(host = operate['data']['host'], port = operate['data']['port'],
                passwds = operate['data']['password'], threadsNum = operate['data']['threadsNum'])

    elif operate['toolName'] == "ssh":
        sshMain(operate['data']['host'], operate['data']['port'], operate['data']['username'],
                operate['data']['password'], operate['data']['threadsNum'])

    elif operate['toolName'] == "subdomain":
        subdomainsMain(operate['data']['domainName'], operate['data']['subdomains'],
                operate['data']['threadsNum'])
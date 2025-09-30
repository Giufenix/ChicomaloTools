#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : cmtools.py
@Author : Chico Malo
@Time : 2025/9/17 19:06  
@脚本说明 : 
"""


import argparse
import random
from getTools import useTools
from resource.commoncolors import Colors
from resource.mnzneuxlog import *

# log展示
logs = [banner1,banner2,banner3,banner4,banner5]
log = random.choice(logs)
version = """
        v(bata 0.3.8)    By 万能小魏 & ChicoMalo & MnznEux


"""
log = log + version
logColor = random.choice(Colors.logColors)
print(f"{logColor}{Colors.BOLD}{log}{Colors.RESET}")

# 项目名称
parser = argparse.ArgumentParser(description="CM安全工具")
subparsers = parser.add_subparsers(help="选择要使用的功能( --help：获取帮助)", dest="sub_command")

ip_subparsers = subparsers.add_parser("ip", help="主机相关漏扫")
ip_subparsers.add_argument("--host", "-H", dest="host", type=str, default="127.0.0.1", help="IP地址")
ip_subparsers.add_argument("--netmask", "-N", dest="netmask", type=str, default="24", help="子网掩码")
ip_subparsers.add_argument("--threads", "-T", dest="threadsNum", type=int, default=100, help="线程数")

port_subparsers = subparsers.add_parser("port", help="端口相关漏扫")
port_subparsers.add_argument("--host", "-H", dest="host", type=str, default="127.0.0.1", help="IP地址")
port_subparsers.add_argument("--threads", "-T", dest="threadsNum", type=int, default=1000, help="线程数")
port_subparsers.add_argument("--interval", "-I", dest="interval", type=int, default=10, help="单线程任务数")

mysql_subparsers = subparsers.add_parser("mysql", help="MySQL相关漏扫")
mysql_subparsers.add_argument("--host", "-H", dest="host", type=str, default="127.0.0.1", help="MySQL主机地址")
mysql_subparsers.add_argument("--port", "-P", dest="port", type=int, default=3306, help="MySQL端口号")
mysql_subparsers.add_argument("--username", "-u", dest="username", type=argparse.FileType(mode='r', encoding="utf-8"),
                                default="./resource/user.dict", help="MySQL用户名")
mysql_subparsers.add_argument("--password", "-p", dest="password", type=argparse.FileType(mode='r', encoding="utf-8"),
                                default="./resource/passwd.dict", help="MySQL密码本")
mysql_subparsers.add_argument("--threads", "-T", dest="threadsNum", type=int, default=1000, help="线程数")

redis_subparsers = subparsers.add_parser("redis", help="Redis相关漏扫")
redis_subparsers.add_argument("--host", "-H", dest="host", type=str, default="127.0.0.1", help="Redis主机地址")
redis_subparsers.add_argument("--port", "-P", dest="port", type=int, default=6379, help="Redis端口号")
redis_subparsers.add_argument("--password", "-p", dest="password", type=argparse.FileType(mode='r', encoding="utf-8"),
                                default="./resource/passwd.dict", help="Redis密码本")
redis_subparsers.add_argument("--threads", "-T", dest="threadsNum", type=int, default=1000, help="线程数")

ssh_subparsers = subparsers.add_parser("ssh", help="SSH相关漏扫")
ssh_subparsers.add_argument("--host", "-H", dest="host", type=str, default="127.0.0.1", help="SSH主机地址")
ssh_subparsers.add_argument("--port", "-P", dest="port", type=int, default=22, help="SSH端口号")
ssh_subparsers.add_argument("--username", "-u", dest="username", type=argparse.FileType(mode='r', encoding="utf-8"),
                                default="./resource/user.dict", help="SSH用户名")
ssh_subparsers.add_argument("--password", "-p", dest="password", type=argparse.FileType(mode='r', encoding="utf-8"),
                                default="./resource/passwd.dict", help="SSH密码本")
ssh_subparsers.add_argument("--threads", "-T", dest="threadsNum", type=int, default=1000, help="线程数")

subdomain_subparsers = subparsers.add_parser("subdomain", help="子域名相关漏扫")
subdomain_subparsers.add_argument("--domain", "-D", dest="domainName", type=str, default="baidu.com", help="域名")
subdomain_subparsers.add_argument("--subdomains", "-S", dest="subdomains", type=argparse.FileType(mode='r', encoding="utf-8"),
                                default="./resource/subdomainsdict.txt", help="子域名字典")
subdomain_subparsers.add_argument("--threads", "-T", dest="threadsNum", type=int, default=1000, help="线程数")

args = parser.parse_args()
if args.sub_command == "ip":
    tool = {
        'toolName': 'ip',
        'data': {'nodeIP': args.host, 'netmask': args.netmask, 'threadsNum': args.threadsNum}
    }
    useTools(tool)

elif args.sub_command == "port":
    tool = {
        'toolName': 'port',
        'data': {'host': args.host, 'threadsNum': args.threadsNum, 'interval': args.interval}
    }
    useTools(tool)

elif args.sub_command == "mysql":
    tool = {
        'toolName':'mysql',
        'data':{
            'host':args.host,'port':args.port,'username':args.username.readlines(),
            'password':args.password.readlines(),'threadsNum':args.threadsNum
        }
    }
    useTools(tool)

elif args.sub_command == "redis":
    tool = {
        'toolName': 'redis',
        'data': {
            'host': args.host, 'port': args.port, 'password': args.password.readlines(),
            'threadsNum': args.threadsNum
        }
    }
    useTools(tool)

elif args.sub_command == "ssh":
    tool = {
        'toolName': 'ssh',
        'data': {
            'host': args.host, 'port': args.port, 'username': args.username.readlines(),
            'password': args.password.readlines(), 'threadsNum': args.threadsNum
        }
    }
    useTools(tool)

elif args.sub_command == "subdomain":
    tool = {
        'toolName': 'subdomain',
        'data': {
            'domainName': args.domainName, 'subdomains': args.subdomains.readlines(),
            'threadsNum': args.threadsNum
        }
    }
    useTools(tool)
else:
    print("选择要使用的功能( --help：获取帮助)\n\n\n")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : scanip.py.py
@Author : Chico Malo
@Time : 2025/9/17 19:08  
@脚本说明 : 
"""

import concurrent.futures
import ipaddress
import warnings
from scapy.interfaces import show_interfaces
from scapy.layers.l2 import ARP
from scapy.sendrecv import sr1

warnings.filterwarnings("ignore")
def getInterfaces():
    print("可选择网卡信息：")
    print("=" * 80)
    show_interfaces()

def scanIp(pdst="127.0.0.1", iface= None):
    try:
        scanIpPkg = ARP(pdst=pdst)
        resultPkg = sr1(scanIpPkg, iface=iface, verbose=False, timeout=0.1)
        if resultPkg:
            psrc = resultPkg.sprintf("%ARP.psrc%")
            pmack = resultPkg.sprintf("%ARP.hwsrc%")
            print(f"[+] {psrc} | {pmack} 存活")
    except Exception as e:
        f"IP扫描出错：{e}"
        pass

def getIp(cidrIp,threadsNum):
    ipList = ipaddress.ip_network(cidrIp,strict=False)
    getInterfaces()
    print("请输入网卡名：")
    iface = input()
    print("正在扫描...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadsNum) as executor:
        for pdst in ipList:
            executor.submit(scanIp, str(pdst), iface)

def ipMain(nodeIP, netmask, threadsNum):
    cidrIp = nodeIP + "/" + netmask
    getIp(cidrIp, threadsNum)

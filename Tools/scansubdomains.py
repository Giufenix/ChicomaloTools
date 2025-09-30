#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : scansubdomains.py
@Author : Chico Malo
@Time : 2025/9/17 19:10  
@脚本说明 : 
"""


import concurrent.futures
import warnings
import requests

warnings.filterwarnings("ignore")

def scanSubdomains(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url,headers=headers, timeout=0.5, verify=False)
        if 200 <= response.status_code < 600:
            print(f"[+] 子域名 {url} 存在")
    except Exception as e:
        f"子域名扫描出错：{e}"
        pass

def subdomainsMain(domainName, subdomains, threadsNum):
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadsNum) as executor:
        for subdomain in subdomains:
            subdomain = subdomain.strip()
            # print(subdomain)
            threadsNum = threadsNum
            url = "http" + f"://{subdomain}.{domainName}"
            executor.submit(scanSubdomains, url)

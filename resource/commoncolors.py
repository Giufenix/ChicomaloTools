#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
@Project : ChicomaloTools
@File : commoncolors.py
@Author : Chico Malo
@Time : 2025/9/17 19:10  
@脚本说明 : 
"""


# 定义颜色代码
class Colors:
    # 重置所有属性
    RESET = "\033[0m"
    # 文本颜色
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    # 高亮文本颜色
    BLACK_BRIGHT = "\033[90m"
    RED_BRIGHT = "\033[91m"
    GREEN_BRIGHT = "\033[92m"
    YELLOW_BRIGHT = "\033[93m"
    BLUE_BRIGHT = "\033[94m"
    MAGENTA_BRIGHT = "\033[95m"
    CYAN_BRIGHT = "\033[96m"
    WHITE_BRIGHT = "\033[97m"
    # 背景颜色
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    # 文本样式
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"  # 反转前景色和背景色

    logColors = [
        BLACK,
        RED,
        GREEN,
        YELLOW,
        BLUE,
        MAGENTA,
        CYAN,
        WHITE,
        BLACK_BRIGHT,
        RED_BRIGHT,
        GREEN_BRIGHT,
        YELLOW_BRIGHT,
        BLUE_BRIGHT,
        MAGENTA_BRIGHT,
        CYAN_BRIGHT,
        WHITE_BRIGHT,
        BOLD,
        UNDERLINE,
        REVERSE
    ]
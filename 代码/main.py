# coding=utf-8

# pip -m install 软件包   #==版本号
#
#     随机数生成模块
import random

# 猜数字

#   不是系统产生  随机生成
#   金币系统 100 -20  扣完位置

#                   开始 ，结束
ran = random.randint(0, 100)  # []#随机数字
jinbi =100

while True:
    a = input("请输入一个数字")  # str  ""
    jinbi =jinbi-20
    if jinbi <20:
        print("金币不足")
        break
    if a.isdigit():  # 由数字组成的字符串
        a = int(a)
        if a <= 100 and a >= 0:
            if a == ran:
                print("猜对了")
                break
            elif a > ran:
                print("猜大了")
            elif a < ran:
                print("猜小了")
        else:
            print("超出范围")
    else:
        print("非法字符")

#  50  以内 逢7  17 27 14 21

from django.shortcuts import render

# Create your views here.
import psutil
import datetime


def get_ServerInfo():
    # 借鉴这位仁兄的方法 ，连接：https://blog.csdn.net/arnolan/article/details/84936075
    total = psutil.virtual_memory().total / (1024 * 1024)
    free = psutil.virtual_memory().free / (1024 * 1024)
    starttime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    print(total, free, starttime)


def task():
    print('我是定时任务')


# coding:utf-8

import multiprocessing

bind = "127.0.0.1:8001"
# workers 是要启动几个实例 多少个进程  但实际只有一个实例 但可以创建多个进程
workers = multiprocessing.cpu_count() * 2
workers_class = 'gevent'
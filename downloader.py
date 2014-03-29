#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from pyquery import PyQuery
from multiprocessing import dummy
import os
import urllib2
import sys

def task(args):
    if os.system("wget -O %s.mp4 -c %s " % (args[0].encode("utf-8"),
                                        args[1].encode("utf-8"))) != 0:
        sys.stderr.write('\033[1;41m %s 下载失败! \033[1;m' ]]' % args[0])
         
        exit(1)

def download(url,pool):
    #html = urllib2.urlopen(url).read().decode('GBK','ignore')
    pq = PyQuery(url)
    courseList = pq("#list2")
    kv = [
            ( i(".u-ctitle>a").text() , i(".downbtn").attr("href") )
            for i in courseList(".u-even,.u-odd").items()
        ]
    print kv
    pool.map(task, kv)
    pool.close()
    pool.join()


def run():
    while 1:
        URL = raw_input("请输入公开课主页面的URL:")
        POOL = dummy.Pool(5)
        download(URL,POOL)
        choice = raw_input("继续(y/n):")
        if choice != "Y" or choice != "y":
            exit(0)

if __name__ == "__main__" :
    run()

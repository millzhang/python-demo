import urllib.request
import re
from pyquery import PyQuery as pq
from proxy import Proxy
import threading
import time
import sys
import queue

# from logger import Logger


# logger = Logger("格言网-爬虫模块")
class Crawler():
    def __init__(self, setting, db):
        # 当前类别下所有待爬链接的列表
        self.domain = "http://www.gexings.com/"
        self.db = db
        self.setting = setting
        self.urlqueue = queue.Queue()

    # # 爬取链接内对应的值
    # def getContentFromUrl(self, catetory, url):
    #     req = urllib.request.Request(url)
    #     req.add_header(
    #         'User-Agent',
    #         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    #     )
    #     try:
    #         data = urllib.request.urlopen(req, timeout=10).read()
    #     except Exception as e:
    #         print("链接超时了" + str(e))
    #     d = pq(data)
    #     result = d('.content>p')
    #     for item in result.items():
    #         item.find('u').remove()
    #         item_str = str(item.text()).strip()
    #         item_arr = item_str.split('\n')
    #         for s in item_arr:
    #             if s != '':
    #                 self.db.insert(catetory, s, url)

    # 执行所有列表爬虫
    def crawlerAll(self):
        for item in self.setting.ss_target:
            urlList = self.getPageUrlList(item)
            for url in urlList:
                if url is not None:
                    self.getContentFromUrl(item["category_cn"], url)

    # 执行测试
    def test(self):
        self.getContentFromUrl("讲点",
                               "http://www.gexings.com/jingdian/44430.html")

    # 主程序，执行
    def run(self):
        # self.crawlerAll()
        # self.test()
        t1 = getUrl(self.urlqueue, self.setting)
        t1.start()

        t2 = getContent(self.urlqueue, self.setting,self.db)
        t2.start()

        t3 = contrl(self.urlqueue)
        t3.start()

# 线程1 获取url地址
class getUrl(threading.Thread):
    def __init__(self, urlqueue, setting):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.setting = setting
        self.domain = "http://www.gexings.com/"

        # 获取当前类别下的链接链表
    def getPageUrlList(self, obj):
        pageSize = self.getPageSize(obj)
        for i in range(1, pageSize):
            url = ""
            if i == 1:
                url = self.domain + obj["category"]
            else:
                url = self.domain + obj["category"] + "/" + obj["prefix"] + "_" + str(
                    i) + ".html"
            html = Proxy(self.setting.proxy_ip, url).run()
            d = pq(html)
            # 获取链接列表
            urlDOMList = d('.title')
            for item in urlDOMList.items():
                url_str = d(item).attr('href')
                if url_str is not None:
                    self.urlqueue.put(url_str)
            print("进程1===>" + obj["category_cn"] + " :====>第" + str(i) +
                  "页列表获取完毕！")

    # 获取首页中显示的页数
    def getPageSize(self, obj):
        url = self.domain + obj["category"]
        html = Proxy(self.setting.proxy_ip,url).run()
        d = pq(html)
        # 获取总页数
        pageSize = d.find('.pageinfo>strong:first-child').html()
        print("进程1===>" + obj["category_cn"] + "共有" + pageSize + "页")
        return int(pageSize)

    def run(self):
        print('获取url，线程启动啦')
        for item in self.setting.ss_target:
            print(item)
            self.getPageUrlList(item)

# 线程2 获取内容
class getContent(threading.Thread):
    def __init__(self, urlqueue, setting,db):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.setting = setting
        self.db = db

    # 爬取链接内对应的值
    def getContentFromUrl(self, url):
        try:
            data = Proxy(self.setting.proxy_ip, url).run()
            d = pq(data)
            result = d('.content>p')
            for item in result.items():
                item.find('u').remove()
                item_str = str(item.text()).strip()
                item_arr = item_str.split('\n')
                for s in item_arr:
                    if s != '':
                        self.db.insert(self.getCategoryFromUrl(url), s, url)
        except Exception as e:
            print("进程2==>链接超时了," + str(e))


    def getCategoryFromUrl(self,url):
        result = ""
        for item in self.setting.ss_target:
            if item["category"] in url:
                result = item["category_cn"]
                break
        return result

    def run(self):
        print('获取内容，线程启动啦')
        while True:
            try:
                url = self.urlqueue.get()
                self.getContentFromUrl(url)
                print("进程2，地址===>"+url+"，执行完毕！")
            except Exception as e:
                print("进程2异常===>" + str(e))


# 控制线程
class contrl(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue

    def run(self):
        while True:
            print("程序执行中...")
            time.sleep(60)
            if self.urlqueue.empty():
                print("程序执行完毕")
                sys.exit()
                os._exit()

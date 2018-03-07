import urllib.request
import re
from pyquery import PyQuery as pq
from setting import Setting
# from logger import Logger

# logger = Logger("格言网-爬虫模块")
class Crawler():
    def __init__(self, setting, db):
        # 当前类别下所有待爬链接的列表
        self.category_url_list = []
        self.domain = setting.domain
        self.db = db
        self.setting = setting

    # 获取首页中显示的页数
    def getPageSize(self, category_url_prefix):
        html = urllib.request.urlopen(category_url_prefix + "_1.html").read()
        d = pq(html)
        # 获取总页数
        pageSize = d.find('.pageinfo>strong:first-child').html()
        return int(pageSize)

    # 获取当前类别下的链接链表
    def getPageUrlList(self, category, category_url_prefix):
        pageSize = self.getPageSize(category_url_prefix)
        pageList = []
        for i in range(1, pageSize):
            html = urllib.request.urlopen(
                category_url_prefix + "_" + str(i) + ".html").read()
            d = pq(html)
            # 获取链接列表
            urlDOMList = d('.title')
            urlList = [
                self.domain + d(url).attr('href')
                for url in urlDOMList.items()
            ]
            pageList.extend(urlList)
            print(category+" :====>第" + str(i) + "页列表获取完毕！")
        return pageList

    # 爬取链接内对应的值
    def getContentFromUrl(self, catetory, url):
        req = urllib.request.Request(url)
        req.add_header(
            'User-Agent',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
        )
        data = urllib.request.urlopen(req).read()
        d = pq(data)
        result = d('.content>p')
        print(result.html())
        for item in result.items():
            result = str(item.html()).strip()
            if result != '':
                self.db.insert(catetory, result, url)

    # 执行所有列表爬虫
    def crawlerAll(self, catetory, prefix_url):
        pageList = self.getPageUrlList(catetory, prefix_url)
        for url in pageList:
            self.getContentFromUrl(catetory, url)

    # 主程序，执行
    def run(self):
        for item in self.setting.target_list:
            category = item["category"]
            category_cn = item["category_cn"]
            prefix = item["prefix"]
            prefix_url = self.domain + "/" + category + "/" + prefix
            self.crawlerAll(category_cn, prefix_url)

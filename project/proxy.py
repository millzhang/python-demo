import urllib.request
import urllib.error
import time

class Proxy():

    def __init__(self,ip,url):
        self.ip = ip
        self.url = url


    def run(self):
        try:
            if self.ip != "":
                proxy = urllib.request.ProxyHandler({'http':self.ip})
                opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
                urllib.request.install_opener(opener)
            req = urllib.request.Request(self.url)
            req.add_header(
                'User-Agent',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
            )
            data = urllib.request.urlopen(req, timeout=10).read()
            return data
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)
            time.sleep(5)
        except Exception as e:
            time.sleep(1)
            print("代理读取url异常："+str(e))
        
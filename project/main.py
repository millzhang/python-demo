from setting import Setting
from db import db_operate
# from crawler import Crawler
from crawler_shuoshuo import Crawler

def run():
    # 数据库初始化,配置初始化
    setting = Setting()
    db = db_operate(setting)
    craw = Crawler(setting, db)
    craw.run()


run()
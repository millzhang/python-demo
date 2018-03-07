import pymysql
import time
# from logger import Logger

# logger = Logger("格言网-数据库模块")

class db_operate():
    """数据库操作"""

    # 初始化连接
    def __init__(self, setting):
        db = pymysql.connect(
            host=setting.db_info['host'],
            user=setting.db_info['user'],
            password=setting.db_info['password'],
            db=setting.db_info['dbname'],
            use_unicode=True,
            charset="utf8")
        print("===数据库连接成功===")
        cur = db.cursor()
        self.db = db
        self.cur = cur
        self.setting = setting

    # 执行数据插入操作
    def insert(self, category, content, url):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                     time.localtime(time.time()))
        sql_insert = "insert into geyan(category,content,url,create_time) values('" + category + "','" + content + "','" + url + "','" + current_time + "')"
        print("执行插入操作，sql语句=>" + sql_insert)
        try:
            self.cur.execute(sql_insert)
            self.db.commit()
        except Exception as e:
            print("数据库插入操作异常=>" + str(e))
            self.db.rollback()
        finally:
            # self.db.close()
            pass

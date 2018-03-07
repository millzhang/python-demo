class Setting():
    def __init__(self):
        self.db_info = {
            "host": "111.231.110.59",
            "user": "root",
            "password": "timepack_206",
            "dbname": "weibo"
        }

        self.target_list = [{
            "category": "lizhimingyan",
            "prefix": "list_33",
            "category_cn": "励志名言"
        }, {
            "category": "renshenggeyan",
            "prefix": "list_32",
            "category_cn": "人生格言"
        }, {
            "category": "mingyanjingju",
            "prefix": "list_37",
            "category_cn": "名言警句"
        }, {
            "category": "html/mingrenmingyan",
            "prefix": "list_1",
            "category_cn": "名人名言"
        }, {
            "category": "html/dushumingyan",
            "prefix": "list_5",
            "category_cn": "读书名言"
        }, {
            "category": "html/jingdianmingyan",
            "prefix": "list_2",
            "category_cn": "经典名言"
        }, {
            "category": "html/aiqingmingyan",
            "prefix": "list_3",
            "category_cn": "爱情名言"
        }, {
            "category": "html/jingdianduanju",
            "prefix": "list_9",
            "category_cn": "经典短句"
        }, {
            "category": "html/renshenggeyan",
            "prefix": "list_4",
            "category_cn": "人生格言2"
        }]

        self.domain = "https://www.geyanw.com"

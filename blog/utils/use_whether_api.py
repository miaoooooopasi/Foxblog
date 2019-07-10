from django.contrib.sites import requests


class Whether:
    """
    处理名人名言接口返回的数据
    """
    def __init__(self):
        """
        初始化相关数据,包括接口的url,headers和parm
        :return: None
        """
        self.url = 'http://api.avatardata.cn/Weather/Query?key=3a9c99ecb5f14a05aac9b27cdf7a14ed&cityname=武汉'
        self.parm = {
            "dtype": "JSON",
        }

    def get_mrmy(self):
        """
        从接口获取名人名言数据,随机选取一条返回,返回json数据.
        :return:json, 名人名言数据
        """
        wb_data = requests.get(self.url, params=self.parm)
        data = wb_data.json()
        print(data)
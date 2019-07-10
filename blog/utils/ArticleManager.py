from django.db import models


class BlogManager(models.Manager):
    def distinct_date(self):  # 该管理器定义了一个distinct_date方法，目的是找出所有的不同日期
        distinct_date_list = []  # 建立一个列表用来存放不同的日期 年-月
        date_list = self.values('create_time')  # 根据文章字段date_publish找出所有文章的发布时间
        for date in date_list:  # 对所有日期进行遍历，当然这里会有许多日期是重复的，目的就是找出多少种日期
            date = date['create_time'].strftime('%Y/%m')  # 取出一个日期改格式为 ‘xxx年/xxx月 存档’
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list
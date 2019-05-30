import datetime

import markdown
from django.shortcuts import render
from haystack import indexes
from .models import Blogs


class BlogsIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索Note，所以创建NoteIndex
    text = indexes.CharField(document=True, use_template=True,
                             template_name='search/indexes/blogs/blogs_text.txt')  # 创建一个text字段

    content = indexes.CharField(model_attr='content')  # 创建一个author字段

    # pub_date = indexes.DateTimeField(model_attr='pub_date')  # 创建一个pub_date字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return Blogs

    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        all = self.get_model().objects.all()
        for blog in all:
            blog.content = markdown.markdown(blog.content)
        return all



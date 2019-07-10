from django.db import models

# Create your models here.
from django.utils import timezone
from mdeditor.fields import MDTextField  # 必须导入

from django.db import models
from django.utils import timezone
from datetime import datetime
from stdimage.models import StdImageField
from .utils.ArticleManager import BlogManager

class Category(models.Model):
    """
    文章的分类
    """

    category_choice = (
        (0, 'python3'),
        (1, 'django'),
        (2, 'flask'),
        (3, '算法'),
        (4, '爬虫'),
    )

    category_name = models.CharField(max_length=20, verbose_name='文章类名')
    category_number = models.IntegerField(default=1, verbose_name='分类数目')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = "文章分类"
        # ordering = ['-c_time']


class Tags(models.Model):
    """
    标签
    """
    tag_name = models.CharField(max_length=20, verbose_name='标签名')
    tag_number = models.IntegerField(default=1, verbose_name='分类数目')

    class Meta:
        verbose_name = '标签页'
        verbose_name_plural = "标签"

    def __str__(self):
        return self.tag_name


class UploadImage(models.Model):
    """上传图片功能"""
    name = models.CharField(max_length=30, verbose_name="名称", default="")  # 标题
    image = StdImageField(max_length=100,
                          upload_to='path/to',
                          verbose_name=u"传图片",
                          variations={'thumbnail': {'width': 100, 'height': 75}})
    # 时间可编辑
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def url(self):
        if self.image:
            return self.image.url
        else:
            return "url为空"

    def image_img(self):
        if self.image:
            href = self.image.url  # 点击后显示的放大图片
            src = self.image.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="传图片"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return '上传图片'

    image_img.short_description = '图片'
    image_img.allow_tags = True  # 列表页显示图片

    class Meta:
        verbose_name = "传图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blogs(models.Model):
    """
    博文
    """
    title = models.CharField(max_length=256, verbose_name=u'标题')
    content = MDTextField(default='', verbose_name=u'正文')
    create_time = models.DateTimeField(default=timezone.now, verbose_name=u'创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'文章类别')
    tags = models.ManyToManyField(Tags, verbose_name=u'文章标签', blank=True)
    img = models.OneToOneField(UploadImage, verbose_name=u'封面', on_delete=models.CASCADE, null=True)
    objects = BlogManager()   # 在模型中使用自定义的管理器

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = "博文"
        ordering = ['-create_time']


class Comment(models.Model):
    """
    评论
    """
    name = models.CharField(max_length=20, default=u'佚名', verbose_name=u'姓名')
    content = models.TextField(verbose_name=u'内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, verbose_name=u'博客')

    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = "评论"
        ordering = ['-create_time']

    def __str__(self):
        return self.name


class Timeaxi(models.Model):
    """
    时间轴
    """
    title = models.CharField(max_length=256, verbose_name=u'标题')
    content = models.TextField(default='', verbose_name=u'正文')
    create_time = models.DateTimeField(default=timezone.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = '时间轴'
        verbose_name_plural = "时间轴"
        ordering = ['-create_time']

    def __str__(self):
        return self.title




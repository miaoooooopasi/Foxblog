from django.db import models

# Create your models here.


class ServerInfo(models.Model):
    """
    服务器信息
    """
    title = models.CharField(max_length=256, verbose_name=u'标题')
    content = MDTextField(default='', verbose_name=u'正文')
    create_time = models.DateTimeField(default=timezone.now, verbose_name=u'生成时间')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'文章类别')
    tags = models.ManyToManyField(Tags, verbose_name=u'文章标签', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = "服务器"
        ordering = ['-create_time']

import xadmin

from .models import *
from xadmin import views
from .models import UploadImage


class CategoryAdmin(object):
    model_icon = 'fa fa-bar-chart'


class TagsAdmin(object):
    model_icon = 'fa fa-asterisk'


class BlogsAdmin(object):
    style_fields = {'tags': 'checkbox-inline', }
    model_icon = 'fa fa-file-text'
    list_filter = ('title', 'content')
    search_fields = ('title', 'content')
    refresh_times = (10, 30)
    list_display = ["title", "create_time", "modify_time", "click_nums", "category", "tags"]


class CommentAdmin(object):
    model_icon = 'fa fa-home'
    data_charts = {
        "user_count": {"title": u"data charts", "x-field": "create_time", "y-field": ("name",)}
    }
    search_fields = ("name",)


class TimeaxiAdmin(object):
    model_icon = 'fa fa-arrows'
    list_filter = ('title', 'content', 'create_time')


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tags, TagsAdmin)
xadmin.site.register(Blogs, BlogsAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Timeaxi, TimeaxiAdmin)


class GlobalSettings(object):
    site_title = 'Foxblog'
    site_footer = '技术支持 @Mr\'ji'
    menu_style = 'accordion'  # 左边导航栏 收缩 手风琴


xadmin.site.register(views.CommAdminView, GlobalSettings)


# xadmin 主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True  # 调出主题菜单


xadmin.site.register(views.BaseAdminView, BaseSetting)


class ControlImage(object):
    # 显示不要用image，而应该用image_img
    list_display = ['name', 'image_img', 'url', 'add_time']


xadmin.site.register(UploadImage, ControlImage)

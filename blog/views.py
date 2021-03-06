from django.shortcuts import render
from haystack.views import SearchView

from Foxblog import settings
from .models import Blogs, Category, UploadImage, Timeaxi
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
import markdown

from django.views.generic import ListView
from .utils import use_whether_api


# Create your views here.


# 分页的通用视图类
class categorryView(ListView):
    context_object_name = 'contacts'
    template_name = 'blog/homepage.html'
    paginate_by = 1
    model = None


# 主页分页
class homepageView(categorryView):
    context_object_name = 'contacts'
    template_name = 'blog/homepage.html'
    paginate_by = 3
    model = Blogs


# python分页
class pythonView(categorryView):
    context_object_name = 'contacts'
    template_name = 'blog/homepage.html'
    paginate_by = 3
    model = Blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = 'python'
        return context


def homepage(request):
    all_blogs = Blogs.objects.all()
    # 循环处理查询结果set里的 content 转换为html
    for blog in all_blogs:
        blog.content = markdown.markdown(blog.content)
    # 分页  每页三篇
    paginator = Paginator(all_blogs, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    top_5 = Blogs.objects.order_by('-click_nums')[0:6]

    archive_list = Blogs.objects.distinct_date()  # 文章归档 获取到的列表格式为： xxx年/xxx月 存档

    return render(request, 'blog/homepage.html', {'contacts': contacts, 'top_5': top_5, 'archive_list': archive_list})


def detail(request, blog_id):
    easy = get_object_or_404(Blogs, id=blog_id)

    # 增加点击数
    # 时间 2019/05/23
    num = Blogs.objects.get(id=blog_id)  # 获得该项
    num.click_nums += 1
    num.save()  # 保存

    # 将markdown转换为HTML
    easy.content = markdown.markdown(easy.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.toc',
        'markdown.extensions.codehilite',
    ],
                                     )
    # 查询博文的标签
    tags = Blogs.objects.filter(id=blog_id).first().tags.all()  # 多对的的查询

    context = {'easy': easy, 'tags': tags}
    return render(request, 'blog/show_blog_easy.html', context=context)


# 分类视图
def category(request):
    python_first_blog = Blogs.objects.filter(category_id=2).first()
    web_first_blog = Blogs.objects.filter(category_id=3).first()
    spider_first_blog = Blogs.objects.filter(category_id=4).first()
    context = {'python': python_first_blog, 'web': web_first_blog, 'spider': spider_first_blog}
    return render(request, 'blog/category.html', context=context)


# python分类视图
def categoryofpython(request):
    python = Blogs.objects.filter(category_id=2)
    # 循环处理查询结果set里的 content 转换为html
    for blog in python:
        blog.content = markdown.markdown(blog.content)
    # 分页  每页三篇
    paginator = Paginator(python, 3)
    page = request.GET.get('page', 1)
    contacts = paginator.get_page(page)
    context = {'pythons': contacts}
    return render(request, 'blog/categoryofpython.html', context=context)


# web
def categoryofweb(request):
    web = Blogs.objects.filter(category_id=3)
    # 循环处理查询结果set里的 content 转换为html
    for blog in web:
        blog.content = markdown.markdown(blog.content)

    paginator = Paginator(web, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {'webs': contacts}

    return render(request, 'blog/categoryofweb.html', context=context)


# spider
def categoryofspider(request):
    spider = Blogs.objects.filter(category_id=4)
    # 循环处理查询结果set里的 content 转换为html
    for blog in spider:
        blog.content = markdown.markdown(blog.content)
    paginator = Paginator(spider, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'spiders': contacts}
    return render(request, 'blog/categoryofspider.html', context=context)


# talkabout:id=5
def categoryoftalkabout(request):
    talkabouts = Blogs.objects.filter(category_id=5)
    # 循环处理查询结果set里的 content 转换为html
    for blog in talkabouts:
        blog.content = markdown.markdown(blog.content)
    paginator = Paginator(talkabouts, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'talkabout': contacts}
    return render(request, 'blog/categoryoftalkabout.html', context=context)


# timeline
def timeline(request):
    timeaxi = Timeaxi.objects.all()
    context = {'timeaxi': timeaxi}
    return render(request, 'blog/timeline.html', context=context)


# about
def about(request):
    return render(request, 'blog/about.html')


# spider
def talkabout(request):
    talkabout = Blogs.objects.filter(category_id=8)
    # 循环处理查询结果set里的 content 转换为html
    for blog in talkabout:
        blog.content = markdown.markdown(blog.content)
    paginator = Paginator(talkabout, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {'contacts': contacts}
    return render(request, 'blog/homepage.html', context=context)


# 搜索引擎 全站搜索
'''
class MySearchView(SearchView):
    """My custom search view."""

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        # further filter queryset based on some set of criteria
        return queryset.filter(pub_date__gte=date(2015, 1, 1))

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        return context
'''


# 按时间归档分类视图
def archive(request):
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)   # 取出两个参数 year,month
    print(year,month)
    # 根据参数year,month进行过滤， 记得字段名+__icontains表大小写不敏感的包含匹配
    blogs = Blogs.objects.filter(create_time__icontains=year + '-' + month)
    # 循环处理查询结果set里的 content 转换为html
    for blog in blogs:
        blog.content = markdown.markdown(blog.content)
    # 分页  每页三篇
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page', 1)
    contacts = paginator.get_page(page)
    context = {'pythons': contacts}
    return render(request, 'blog/categoryofpython.html', context=context)

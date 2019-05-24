from django.shortcuts import render
from .models import Blogs, Category, UploadImage, Timeaxi
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
import markdown

from django.views.generic import ListView

# Create your views here.


# 分页的通用视图
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
    return render(request, 'blog/homepage.html', {'contacts': contacts})


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

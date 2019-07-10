"""Foxblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf.urls import include

from django.urls import path, re_path



from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('category/', views.category, name='category'),
    path('category/python', views.categoryofpython, name='python'),
    path('category/web', views.categoryofweb, name='web'),
    path('category/spider', views.categoryofspider, name='spider'),
    path('timeline/', views.timeline, name='timeline'),
    path('about/', views.about, name='about'),
    path('talkabout/', views.categoryoftalkabout, name='talkabout'),
    # path('search/', MySearchIndex(), name='haystack_search'),
    # path('category/<int:year>/<int:month>/', views.categoryoftime, name='categoryoftime'),
    url(r'^archive/$', views.archive, name='archive'),

    # path('top_5/', views., name="top_5"),
]



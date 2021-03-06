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
from Foxblog import settings
from django.conf.urls.static import static

from django.urls import path, re_path
from django.views.static import serve
import xadmin


urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('mdeditor/', include('mdeditor.urls')),
    path('^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    path('blog/', include('blog.urls', namespace='blog')),
    path('search/', include('haystack.urls')),



]



if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

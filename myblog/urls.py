# -*- coding:utf-8 -*-
"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from myblog.settings import MEDIA_ROOT, STATIC_ROOT
from blog01.views import IndexView, BlogContentView,AddArticleView,ListArticleView,AboutView,LiuyanView,SearchView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^article/(?P<blog_id>\d+)', BlogContentView.as_view(), name="article"),

    url(r'^add_article/$', AddArticleView.as_view(), name="add_article"),
    #展示当前分类的文章列表信息
    url(r'^list_article/(?P<type>.*)/$', ListArticleView.as_view(), name="list_article"),
    #展示个人信息
    url(r'^myself/$', AboutView.as_view(), name='myself'),
    #留言板
    url(r'^liuyan/$', LiuyanView.as_view(), name='liuyan'),
    #搜索
    url(r'^search/$', SearchView.as_view(), name='search'),

    #配置uediter富文本编辑器路径
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    #配置文件上传
    url(r'^media/(?P<path>.*)$', serve , {'document_root':MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),
]

from blog01.views import *
handler404 = page_not_found
handler500 = page_error
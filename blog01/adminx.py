# -*- coding: utf-8 -*-
__author__ = 'sachin'
__date__ = '2017/9/4 11:22'

import xadmin
from xadmin import views
from .models import UserProfile, BlogCategory, BlogPost


# class UserProfileView(object):
#     list_display = ['name', 'desc', 'image','add_time']
#     search_fields = ['name', 'desc', 'image']
#     list_filter = ['name', 'desc', 'image','add_time']

class BaseSetting(object):
    """
    定义主题
    """
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = '个人博客后台管理系统'
    site_footer = '个人博客'
    menu_style = 'accordion'


class BlogCategoryView(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class BlogPostView(object):
    list_display = ['category', 'title', 'add_time']
    search_fields = ['category', 'title']
    list_filter = ['category', 'title', 'add_time']
    style_fields = {'content':'ueditor'}

# xadmin.site.register(UserProfile, UserProfileView)
xadmin.site.register(BlogCategory, BlogCategoryView)
xadmin.site.register(BlogPost, BlogPostView)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
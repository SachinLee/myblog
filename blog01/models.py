# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.


class UserProfile(AbstractUser):
    name = models.CharField(max_length=20, verbose_name=u"用户名", default="")
    desc = models.TextField(verbose_name="个人简介")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"文章类别")
    desc = models.CharField(max_length=200, verbose_name=u"分类描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章类别信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class BlogPost(models.Model):
    category = models.ForeignKey(BlogCategory, verbose_name=u"文章类别")
    title = models.CharField(max_length=100, verbose_name=u"文章标题")
    # content = models.TextField(verbose_name=u"文章内容")
    content = UEditorField(verbose_name=u"文章内容", width=600, height=300, toolbars="full",
                          imagePath="blog/ueidtor/", filePath="blog/ueidtor/",default='')
    poll_num = models.IntegerField(default=0, verbose_name=u"点击量")
    comment_num = models.IntegerField(default=0, verbose_name=u"评论数量")
    keep_num = models.IntegerField(default=0, verbose_name=u"收藏数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章内容信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

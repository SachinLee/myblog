# -*- coding: utf-8 -*-
__author__ = 'sachin'
__date__ = '2017/9/5 12:39'

from  django import forms
from DjangoUeditor.forms import UEditorField
from datetime import datetime

class ArticleForm(forms.Form):
    category = forms.CharField(label=u"类别")
    title = forms.CharField(max_length=100, label=u"文章标题")
    content = UEditorField(label=u"文章内容",width=1000, height=300, imagePath="ueitor/image",
                           toolbars='full', filePath='ueitor/image')
    poll_num = forms.IntegerField(label=u"点击量")
    comment_num = forms.IntegerField(label=u"评论数量")
    keep_num = forms.IntegerField(label=u"收藏数量")
    add_time = forms.DateTimeField(label=u"添加时间")

class SearchForm(forms.Form):
    article_name = forms.CharField()
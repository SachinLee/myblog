# -*- coding: utf-8 -*-
__author__ = 'sachin'
__date__ = '2017/9/5 19:40'

import xadmin
from xadmin.views import BaseAdminPlugin,CreateAdminView,ModelFormAdminView, UpdateAdminView
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from django.conf import settings
import os


class XadminUeditorWidget(UEditorWidget):
    def __init__(self, **kwargs):
        self.ueditor_options = kwargs
        self.Media.js = None
        super(XadminUeditorWidget, self).__init__(kwargs)


class UeditorPlugin(BaseAdminPlugin):
    def get_field_style(self, attrs, db_field, style, **kwargs):
        if style == 'ueditor':
            if isinstance(db_field, UEditorField):
                widget = db_field.formfield().widget
                param = {}
                param.update(widget.ueditor_settings)
                param.update(widget.attrs)
                return {'widget':XadminUeditorWidget(**param)}
        return attrs

    def block_extrahed(self, content, nodes):
        js = '<script type="text/javascript" src="%s"></script>' % (settings.BASE_DIR + 'DjangoUeditor/static/ueditor/ueditor.config.js')
        js += '<script type="text/javascript" src="%s"></script>' % (settings.BASE_DIR + 'DjangoUeditor/static/ueditor/ueditor.all.min.js')
        nodes.append(js)

xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)
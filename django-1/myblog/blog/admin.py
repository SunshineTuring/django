# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('title', 'content','pup_time')
    # list_filter = ('pup_time',)
    pass


admin.site.register(Article)
# Register your models here.

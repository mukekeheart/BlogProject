#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = custom_site
__author__ = mukekeheart
__mtime__ = 2020/4/11
"""
from django.contrib import admin


class CustomSite(admin.AdminSite):
    site_header = 'blog_project'
    site_title = '博客管理系统后台页面'
    index_title = '首页'


custom_site = CustomSite(name='cus_site')


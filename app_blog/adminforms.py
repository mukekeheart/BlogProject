#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = adminforms
__author__ = mukekeheart
__mtime__ = 2020/4/10
"""

from django import forms


class PostForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)


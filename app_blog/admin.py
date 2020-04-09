from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # 配置列表页面展示哪些字段
    list_display = ('name', 'status', 'is_nav', 'create_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class PostAdmin(admin.ModelAdmin):
    # 展示页面
    # 配置列表页面展示哪些字段
    list_display = ('title', 'category', 'status', 'create_time', 'operator')
    # 配置哪些字段可以作为链接，点击它们，可以进入编辑页面
    list_display_links = []

    # 配置页面过滤器，需要通过哪些字段来过滤列表页
    list_filter = ['category',]
    # 配置搜索字段
    search_fields = ['title', 'category__name']

    # 动作相关的配置，是否展示在顶部
    actions_on_top = True
    # 动作相关的配置，是否展示在底部
    actions_on_bottom = True

    # 编辑页面
    # 保存、编辑、编辑并新建按钮是否在顶部展示
    save_on_top = True

    fields = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:app_blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
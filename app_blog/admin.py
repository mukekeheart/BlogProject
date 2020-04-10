from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post
from BlogProject.custom_site import custom_site
from .adminforms import PostForm



# Register your models here.


class BaseOwnerAdmin(admin.ModelAdmin):
    """
        1. 用来自动补充文章、分类、标签、侧边栏、友链这些 Model 的 owner 字段
        2. 用来针对 queryset 过滤当前用户的数据
    """
    exclude = ('owner',)

    # 重写 get _queryset 方法，让列表页在展示文章或者分类时只展示当前用户的数据
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    # 重写save 方法 ，此时需要设置对象的 owner
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)


class PostInline(admin.TabularInline):
    model = Post
    fields = ('title', 'desc')
    extra = 1


class CategoryAdmin(BaseOwnerAdmin):
    # 配置列表页面展示哪些字段
    list_display = ('name', 'status', 'is_nav', 'create_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    inlines = [PostInline,]

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'create_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category_id=self.value())
        return queryset


class PostAdmin(BaseOwnerAdmin):

    form = PostForm

    # 展示页面
    # 配置列表页面展示哪些字段
    list_display = ('title', 'category', 'status', 'create_time', 'owner', 'operator')
    # 配置哪些字段可以作为链接，点击它们，可以进入编辑页面
    list_display_links = []
    # 配置页面过滤器，需要通过哪些字段来过滤列表页
    list_filter = [CategoryOwnerFilter]
    # 配置搜索字段
    search_fields = ['title', 'category__name']

    # 动作相关的配置，是否展示在顶部
    actions_on_top = True
    # 动作相关的配置，是否展示在底部
    actions_on_bottom = True

    # 编辑页面
    # 保存、编辑、编辑并新建按钮是否在顶部展示
    save_on_top = True
    exclude = ['owner']

    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = [
        ('基础配置', {
            'description':'基础配置描述',
            'fields':(
                ('category', 'title'),
                'status',
            )
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            )
        }),
        ('额外信息', {
            'classes':('wide',),
            'fields': ('tag',)
        }),
    ]

    filter_vertical = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_site:app_blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


custom_site.register(Category, CategoryAdmin)
custom_site.register(Tag, TagAdmin)
custom_site.register(Post, PostAdmin)


# 日志显示
@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr','object_id','action_flag','user', 'change_message']

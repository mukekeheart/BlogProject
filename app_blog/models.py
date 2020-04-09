from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 用户模型 用Django自带的 User


# 分类模型
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_category'
        verbose_name = verbose_name_plural = '分类'


# 标签模型
class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_tag'
        verbose_name = verbose_name_plural = '标签'


# 文章模型
class Post(models.Model):
    STATUS_DRAFT = 2
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_DRAFT, '草稿'),
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正丈必须为 MarkDown 格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_post'
        verbose_name = verbose_name_plural = '文章'
        ordering = ['id']



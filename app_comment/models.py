from django.db import models
from app_blog.models import Post

# Create your models here.


# 评论模型
class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    target = models.ForeignKey(Post, on_delete= models.CASCADE, verbose_name= '目标文章')
    content = models.TextField(max_length=2000,
                               verbose_name='内容',)
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')  # 默认长度是200
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'blog_comment'
        verbose_name = verbose_name_plural = '评论'

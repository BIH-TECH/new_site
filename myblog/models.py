from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse
# Create your models here.

class Tag(models.Model):
    name = models.CharField(u"标签", max_length=16)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(u"分类", max_length=20)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(u"名称", max_length = 30)
    author = models.ForeignKey(User, on_delete = False)
    excerpt = models.CharField(u"摘要",max_length= 40)
    created_time = models.DateTimeField(u"发布时间",auto_now = True)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete = True, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name= u"标签",blank = True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("myblog:detail", kwargs={"pk":self.pk})
    class Meta:
        ordering = ["-created_time"]


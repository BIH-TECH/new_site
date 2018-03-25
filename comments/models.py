from django.db import models

# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length = 255 )
    url = models.URLField(blank = True)
    content = models.TextField()
    Created_time = models.DateTimeField(auto_now_add = True)

    post = models.ForeignKey("myblog.Article", on_delete=False)

    def __str__(self):
        return self.content[:20]


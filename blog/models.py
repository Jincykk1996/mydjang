from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.conf import settings

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='pics', default='sample.jpg')

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='pics', default=None)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    msgcount = models.IntegerField(default=1)
    dimage = models.ImageField(upload_to='pics', default=None, null=True)
    ddescription = models.CharField(max_length=10000, null=True)
    quotes = models.CharField(max_length=1000, null=True)
    qname = models.CharField(max_length=100, null=True)
    content = HTMLField('Content')

    def __str__(self):
        return self.title


class Comment(models.Model):
    field = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.CharField(max_length=10000, null=True)
    cdate = models.DateField(auto_now_add=True, blank=True, null=True)
    cuser = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.comments

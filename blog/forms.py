from .models import Blog, Comment
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('category', 'title', 'description', 'image', 'content', 'dimage', 'ddescription', 'quotes', 'qname')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comments',)

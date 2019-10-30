from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Blog, Author, Comment
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import BlogForm, CommentForm
from django.contrib.auth import get_user_model

User = get_user_model()



def p(request):
    obj = Blog.objects.all()
    lastblogs = Blog.objects.all().order_by('-time')[0:3]

    return render(request, 'bindex.html', {'ob': obj,
                                           'lb': lastblogs})


def p1(request):
    obj = Blog.objects.all()
    paginator = Paginator(obj, 4)
    lastblogs = Blog.objects.all().order_by('-time')[0:3]
    page = request.GET.get('page')
    item = paginator.get_page(page)
    return render(request, 'blog.html', {'ob': item,
                                         'lb': lastblogs})





def p3(request):
    if request.method == 'POST':

        a = request.POST['uname']
        b = request.POST['pwd1']
        c = request.POST['email']
        d = request.POST['pwd2']
        if User.objects.filter(username=a).exists():
            messages.info(request, 'username already exists')
            return redirect('blog:register')
        elif b != d:
            messages.info(request, 'invalid password')
            return redirect('blog:register')
        else:
            user = User.objects.create_user(username=a, password=b, email=c)
            user.save()
            auth.login(request, user)
            return redirect('blog:blog')
    return render(request, 'breg.html')


def p4(request):
    if request.method == 'POST':

        a = request.POST['uname']
        b = request.POST['pwd']
        user = auth.authenticate(username=a, password=b)
        if user is not None:
            auth.login(request, user)
            return redirect('blog:blog')
        else:
            # return redirect('account:login')
            messages.info(request, 'error')
    return render(request, 'blogin.html')


def p5(request):
    auth.logout(request)
    return redirect('blog:blog')


def p6(request, id):
    ob1 = get_object_or_404(Blog, id=id)
    # form = CommentForm(request.POST or None)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.cuser = get_us(request.user)
            form.instance.field = ob1
            # form.instance.author = Author.objects.filter(user=request.user)
            form.save()
            form = CommentForm()

    lastblogs = Blog.objects.all().order_by('-time')[0:3]
    c = Comment.objects.filter(field_id=ob1.id)

    return render(request, 'post.html', {'obj': ob1,
                                         'lb': lastblogs,
                                         'f': form,
                                         'comment': c})


def p7(request):
    lastblogs = Blog.objects.all().order_by('-time')[0:3]
    x = request.GET.get('search')
    if x is not None:
        global v
        v = Blog.objects.filter(category__icontains=x)
    paginator = Paginator(v, 4)
    page = request.GET.get('page')
    item = paginator.get_page(page)
    return render(request, 'bsearch.html', {'lb': lastblogs,
                                            'ob': item})


def get_us(user):
    a = Author.objects.filter(user=user)
    return a[0]


def p8(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            # form.instance.author = Author.objects.filter(user=request.user)
            form.instance.author = get_us(request.user)
            form.save()
        else:
            print('not valid')
    return render(request, 'bcreate.html', {'f': form})


def p9(request, id):
    ob1 = get_object_or_404(Blog, id=id)

    instance = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST':

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect(reverse('blog:bpost', kwargs={'id': instance.id}))

    return render(request, 'bcreate.html', {'f': form, 'obj': ob1})


def p10(request, id):
    instance = get_object_or_404(Blog, id=id)
    instance.delete()

    return redirect('blog:blog')


def p11(request):
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # form.instance.field =
            # form.instance.author = Author.objects.filter(user=request.user)
            form.save()

    return redirect('../')

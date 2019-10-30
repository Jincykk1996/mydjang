from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Products, Cart, Coupon
from django.contrib.auth.models import auth, User
from django.contrib import messages
from datetime import datetime
import numpy as np

from django.db.models import Q


def pro(request):
    obj = Products.objects.all()
    return render(request, 'index.html', {'ob': obj})


def logout(request):
    auth.logout(request)
    return redirect('account:index')


def register(request):
    if request.method == 'POST':

        a = request.POST['uname']
        b = request.POST['pwd1']
        c = request.POST['email']
        d = request.POST['pwd2']
        if User.objects.filter(username=a).exists():
            messages.info(request, 'username already exists')
            return redirect('account:register')
        elif b != d:
            messages.info(request, 'invalid password')
            return redirect('account:register')
        else:
            user = User.objects.create_user(username=a, password=b, email=c)
            user.save()
            auth.login(request, user)
            return redirect('account:index')
    return render(request, 'submit.html')


def login(request):
    if request.method == 'POST':

        a = request.POST['uname']
        b = request.POST['pwd']
        user = auth.authenticate(username=a, password=b)
        if user is not None:
            auth.login(request, user)
            return redirect('account:index')
        else:
            # return redirect('account:login')
            messages.info(request, 'error')
    return render(request, 'login page.html')


def search(request):
    x = request.GET['search']
    v = Products.objects.filter(name__icontains=x)
    # return render(reverse(''))
    return render(request, 'items.html', {'obj': v})


def add_to_cart(request, id):
    cart = get_object_or_404(Products, id=id)
    d = datetime.now()
    price = cart.price
    item = Cart.objects.create(user=request.user, item_id=cart.id, order_date=d, total_price=price)
    return redirect('../')


def cont(request, id):
    if request.method == 'POST':
        cart = Cart.objects.get(id=id)
        q = request.POST['number']
        p = cart.item.price
        total = int(p) * int(q)
        Cart.objects.filter(id=id).update(total_price=total, quantity=q)

    return redirect('account:cart')


def cart(request):
    user = Cart.objects.filter(user=request.user)
    price = 0
    for i in user:
        price = price + i.total_price
    global c
    c=0
    if request.method == 'POST':
        x = request.POST['couponcode']
        # v = Coupon.objects.filter(codes=x)
        v =Coupon.objects.get(codes=x)
        if v is not None:
            c = v
            return render(request, 'cart.html', {'u': user, 'p': price, 'ofr': c})
        else:
            messages.info(request, 'code doesnot exist')
            return render(request, 'cart.html', {'u': user, 'p': price, 'ofr': c})


    return render(request, 'cart.html', {'u': user, 'p':price, 'ofr': c})


def delete(request, id):
    cart_id = get_object_or_404(Cart, id=id)
    cart_id.delete()
    return redirect('account:cart')

def checkout(request):
    return render(request, 'checkout.html')

def coupon(request):
    x = request.POST['couponcode']

    v = Coupon.objects.get(codes=x)
    if v is not None:
        global c
        c = v
    else:
        messages.info(request, 'code doesnot exist')

    return render(request, 'cart.html', {'ofr':c})


    # if Products.objects.filter(name=x).exists():
    #     q = Products.objects.get(name=x)
    #     messages.info(request, q)
    #     return redirect('account:index')
    # else:
    #     messages.info(request, 'not exist')
    #     return redirect('account:index')

from django.shortcuts import render, HttpResponse,Http404,get_object_or_404
from .models import Product


# def forl(request):
    # n1 = ['hello..', 'hai..', 'welcome']
    # # a={'n2':n1}
    # return render(request,'forloop.html',{'n2':n1,'a':True})

    # ob1 = Product.objects.get(id=1)
    # ob2 = Product.objects.get(id=2)
    # ob3 = Product.objects.get(id=3)
    # return render(request, 'pro.html', {'o1': ob1,'o2': ob2,'o3': ob3})

    # ob = Product.objects.all()
    # return render(request, 'pro.html', {'obj':ob})

def prod(request,id):
    # try:
    #     ob1 = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404("hdsbvhj")

    ob1 = get_object_or_404(Product,id=id)


    return render(request, 'tempor.html', {'obj': ob1})
    # return HttpResponse('selected id is %s' %id)


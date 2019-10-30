from django.shortcuts import render,HttpResponse

def form(request):
    return render(request,'form.html')
def result(request):
    uname=['jincy','ashik','anji','mukil','manu']
    pwd=['1','2','3','4','5']
    a=request.POST['uname']
    b=request.POST['pwd']
    print(request.POST)
    print(request.GET)
    if a in uname:
        i=uname.index(a)
        if b in pwd[i]:
            return render(request, 'result.html', {'u': a, 'p': b})
        else:
            return HttpResponse('invalid')
    else:
        return HttpResponse('invalid')

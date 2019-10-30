from django.shortcuts import render,redirect


def log(request):
    if request.method == 'POST':
        a = request.POST['uname']
        b = request.POST['pwd']
        print(a,b)
        return redirect('login')
    else:
        return render(request, 'form.html')

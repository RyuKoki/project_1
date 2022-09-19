from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

# index test
# def home(request):
#     #return HttpResponse("<h2>hello world</h2>")
#     return render(request, 'home.html')

def elder_register(request):
    return render(request, 'elder_regis.html')

def elder_register2(request):
    return render(request, 'elder_regis2.html')

def elder_register3(request):
    return render(request, 'elder_regis3.html')

def elder_register4(request):
    return render(request, 'elder_regis4.html')

def elder_register5(request):
    return render(request, 'elder_regis5.html')
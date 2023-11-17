from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
#def addition(request):
   # x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #return render(request,"result.html",{'result':res})
#def subtraction(request):
       # x = int(request.GET['num1'])
        #y = int(request.GET['num2'])
        #res = x-y
        #return render(request, "result.html", {'result': res})


def multiplication(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x*y
    return render(request, "result.html", {'result': res})


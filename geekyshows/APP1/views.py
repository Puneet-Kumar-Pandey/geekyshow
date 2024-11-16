from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def Fun1(request):
 #   return HttpResponse("<h1>hello</h1>")
def about(request):
    return render(request,'about.html')

def hel(request):
    return HttpResponse('<h1>harshita</h1>')

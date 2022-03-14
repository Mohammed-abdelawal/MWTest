from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request,'mytemplate.html')


def noMore(request):
    return render(request,'error.html')
    
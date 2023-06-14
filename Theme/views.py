from django.shortcuts import render

def HomePage(request):
    return render(request,'index.html')


def ProductPage(request):
    return render(request,'product.html')

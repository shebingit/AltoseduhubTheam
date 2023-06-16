from django.shortcuts import render

def HomePage(request):
    return render(request,'index.html')


def ProductPage(request):
    return render(request,'product.html')

def PricingPage(request):
    return render(request,'pricing.html')

def AboutPage(request):
    return render(request,'about.html')


def ContactPage(request):
    return render(request,'contact.html')
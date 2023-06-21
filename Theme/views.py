from django.shortcuts import render

def HomePage(request):
    return render(request,'index.html')


def ProductPage(request):
    return render(request,'product.html') 

def categoryPage(request):
    return render(request,'category.html')

def TemplateView(request):
    return render(request,'view_template.html')

def PricingPage(request):
    return render(request,'pricing.html')

def AboutPage(request):
    return render(request,'about.html')


def ContactPage(request):
    return render(request,'contact.html')

def BlogPage(request):
    return render(request,'blog.html')
from django.shortcuts import render



def HomePage(request):
    title = "Altos Theme Store"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'index.html',context)


def ProductPage(request):
    title = "Our Products & Services"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'product.html',context) 


def categoryPage(request):
    title = "Best Templates for your site"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'category.html',context)


def TemplateView(request):
    title = "Template Preview"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'view_template.html',context)


def PricingPage(request):
    title = "Plan & Pricing"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'pricing.html',context)

def AboutPage(request):
    title = "Look out who we are?"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'about.html',context)


def ContactPage(request):
    title = "Altos Theme Store\Contact"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'contact.html',context)

def BlogPage(request):
    title = "My Page Title"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."

    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        }
    return render(request,'blog.html',context)
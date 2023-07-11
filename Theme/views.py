from django.shortcuts import render,redirect
from django.core import serializers
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from .models import*



def HomePage(request):
    title = "Altos Theme Store"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    templates = Templates.objects.all()[:5]
    categorie = Categorie.objects.all()
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'templates':templates,'categorie':categorie
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
    categorie=Categorie.objects.all()
    templates=Templates.objects.all()
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'categorie':categorie,
        'templates':templates
        }
    return render(request,'category.html',context)


def TemplateView(request,pk):
    title = "Template Preview"
    meta_tags = ["tag1", "tag2", "tag3"]
    meta_description = "This is the meta description of my page."
    categorie=Categorie.objects.all()
    templates=Templates.objects.all()
    template=Templates.objects.get(id=pk)
    context = {
        'title': title,
        'meta_tags': meta_tags,
        'meta_description': meta_description,
        'categorie':categorie,'template':template,
        'templates':templates
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

#================= User Section End ===============================



#================= Admin section ===================================


def adminlogin(request):
    return render(request,'admin/login.html')

def loginCheck(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
    
        
        if user is not None:
            request.session["uid"]=user.id
            auth.login(request,user)    
            categori_count=Categorie.objects.count()
            template_count = Templates.objects.count()
            page_name='Dashboard'
            return render(request,'admin/dashboard.html',{'page_name':page_name,'categori_count':categori_count,'template_count':template_count})
        else:
            msg='Invalid Username or Password ! Try Again.'
            return render(request, 'admin/login.html',{'msg':msg})


def Dashboard(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        categori_count=Categorie.objects.count()
        template_count = Templates.objects.count()
        page_name='Dashboard'
        return render(request,'admin/dashboard.html',{'page_name':page_name,'categori_count':categori_count,'template_count':template_count})
    else:
        return redirect('adminlogin')
    
    
def categorie_load(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        page_name='Categorie'
        return render(request,'admin/categorie_add.html',{'page_name':page_name})
    else:
        return redirect('adminlogin')
    


def categorie_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
       
        if request.method=='POST':
        
            categorie=Categorie()
            categorie.categorie_name=request.POST['categori_name']
            categorie.status=request.POST.get('visibility_opt')
            categorie.publish_date=request.POST['publish_date']
            categorie.time=request.POST['publish_time']
            categorie.img_alttag=request.POST['tag_name']
            categorie.categorie_image=request.FILES.get('categori_img')
            categorie.save()

            msg= 'Data saved successfully.'
            page_name='Categorie'
            return render(request,'admin/categorie_add.html',{'page_name':page_name,'msg':msg})
    else:
        return redirect('adminlogin')
        

def categorie_edit(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        page_name='Categorie'
        return render(request,'admin/categorie_edit.html',{'page_name':page_name,'categories':categories})
    else:
        return redirect('adminlogin')

def fetch_categori(request):
    value = request.GET.get('value')
    categorie=Categorie.objects.get(id=value)
    image_url = Categorie.objects.values_list('categorie_image', flat=True).get(id=value)
    
    response = {
        'categorie_name': categorie.categorie_name,
        'categorie_tag': categorie.img_alttag,
        'image': image_url,
        'radioValue': int(categorie.status),
        'categorie_date':categorie.publish_date,
        'categorie_time':categorie.time
        
    }
    return JsonResponse(response)


def categeori_edit_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')

        categories=Categorie.objects.all()
        page_name='Categorie'

        if request.method=='POST':
            categorie=Categorie.objects.get(id=request.POST['slect_categori'])
            categorie.categorie_name=request.POST['categori_name']
            categorie.status=request.POST.get('visibility_opt')
            categorie.publish_date=request.POST['publish_date']
            categorie.time=request.POST['publish_time']
            categorie.img_alttag=request.POST['tag_name']
            if request.FILES.get('categori_img'):
                categorie.categorie_image=request.FILES.get('categori_img')
            else:
                categorie.categorie_image = categorie.categorie_image

            categorie.save()
            msg= 'Data Edit successfully.'
            return render(request,'admin/categorie_edit.html',{'page_name':page_name,'categories':categories,'msg':msg})

        else:
    
            return render(request,'admin/categorie_edit.html',{'page_name':page_name,'categories':categories})
    else:
        return redirect('adminlogin')


def categorie_list(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        page_name='Categorie'
        return render(request,'admin/categorie_list.html',{'page_name':page_name,'categories':categories})
    else:
        return redirect('adminlogin')

def template_load(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        page_name='Template'
        return render(request,'admin/template_load.html',{'page_name':page_name,'categories':categories})
    else:
        return redirect('adminlogin')


def template_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        if request.method=='POST':
        
            template=Templates()
            template.categori_id=Categorie.objects.get(id=int(request.POST['slect_categori']))
            template.template_name=request.POST['temp_name']
            template.template_discription=request.POST['temp_discription']
            template.template_status=request.POST.get('radio__inputBox')
            template.template_publish_date=request.POST['publish_date']
            template.template_time=request.POST['publish_time']
            template.template_img_alttag=request.POST['tag_name']
            template.template_rating=request.POST.get('rating_opt')
            template.template_price=request.POST['temp_price']
            template.template_image=request.FILES.get('temp_img')
            template.video_file = request.FILES['temp_video']
            template.save()
            msg= 'Template saved successfully.'
            page_name='Template'
            categories=Categorie.objects.all()
            return render(request,'admin/template_load.html',{'page_name':page_name,'msg':msg,'categories':categories})
    else:
        return redirect('adminlogin')


def template_editload(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        templates=Templates.objects.all()
        page_name='Template'
        return render(request,'admin/template_editlist.html',{'page_name':page_name,'categories':categories,'templates':templates})
    else:
        return redirect('adminlogin')


def fetch_templates(request):
    categories=Categorie.objects.get(id=int(request.GET.get('value')))
    templates=Templates.objects.filter(categori_id=categories)
   
    
    response = {
        'templates':templates
    }
    return JsonResponse(response)


def template_list(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        categories=Categorie.objects.all()
        templates=Templates.objects.all()
        page_name='Template'
        return render(request,'admin/template_list.html',{'page_name':page_name,'categories':categories,'templates':templates})
    else:
        return redirect('adminlogin')


# Admin Account Settings 

def profile(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        user_id=User.objects.get(id=uid)
        try:
            user_check= Admin_data.objects.get(u_id=user_id)

        except Admin_data.DoesNotExist:
            user_check=User.objects.get(id=uid)
        page_name='Account Setting'
        return render(request,'admin/profile.html',{'page_name':page_name,'user_check':user_check})
        
    else:
        return redirect('adminlogin')




def useredit_save(request):

    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
         
        if request.method=='POST':

            user_id=User.objects.get(id=uid)
            try:
                user_check= Admin_data.objects.get(u_id=user_id)
                user_check.u_name=request.POST['fullName']
                user_check.u_desig=request.POST['desig']

                if request.FILES.get('u_img'):
                    user_check.u_image=request.FILES.get('u_img')
                else:
                    user_check.u_image=user_check.u_image
                
                user_check.save()

            except Admin_data.DoesNotExist:
               user_check=Admin_data()
               user_check.u_id=user_id
               user_check.u_name=request.POST['fullName']
               user_check.u_desig=request.POST['desig']
               user_check.u_image=request.FILES.get('u_img')
               user_check.save()
               
        page_name='Account Setting'
        return render(request,'admin/profile.html',{'page_name':page_name,'user_check':user_check})
        
    else:
        return redirect('adminlogin')
    
def user_password_edit(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
        
        user_id=User.objects.get(id=uid)

        try:
            user_check= Admin_data.objects.get(u_id=user_id)
                
        except Admin_data.DoesNotExist:
                user_check=User.objects.get(id=uid)
        page_name='Account Setting'
        return render(request,'admin/password.html',{'page_name':page_name,'user_check':user_check})
        
    else:
        return redirect('adminlogin')


def userpassword_save(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('adminlogin')
         
        if request.method =='POST':

            user_id=User.objects.get(id=uid)
            try:
                user_check= Admin_data.objects.get(u_id=user_id)
                user_id.set_password(request.POST.get('newpassword'))
                user_id.save()
                user_check.u_password=request.POST.get('newpassword')
                user_check.save()

                result_message = "Password Change successfully!"
                
            
            except Admin_data.DoesNotExist:
                user_check=User.objects.get(id=uid)
           
            
        page_name='Account Setting'
        return render(request,'admin/password.html',{'page_name':page_name,'user_check':user_check})
        
    else:
        return redirect('adminlogin')

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    
    return redirect('HomePage')
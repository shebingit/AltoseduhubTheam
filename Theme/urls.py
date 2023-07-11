from django.urls import path 
from.import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('',views.HomePage,name='HomePage'),
    path('Products',views.ProductPage,name='ProductPage'),
    path('Category',views.categoryPage,name='categoryPage'),
    path('Pricing',views.PricingPage,name='PricingPage'),
    path('About',views.AboutPage,name='AboutPage'),
    path('Contact',views.ContactPage,name='ContactPage'),
    path('Blog',views.BlogPage,name='BlogPage'),
    path('Templates/<int:pk>',views.TemplateView,name='TemplateView'),


    # ================ Admin section ===========

    path('login',views.adminlogin,name='adminlogin'),
    path('logout',views.logout,name='logout'),

    path('LgoinCheck',views.loginCheck,name='loginCheck'),
    path('Dashboard',views.Dashboard,name='Dashboard'),
    path('Categorie_Form',views.categorie_load,name='categorie_load'),
    path('Categorie_Save',views.categorie_save,name='categorie_save'),
    path('categorie_Edit',views.categorie_edit,name='categorie_edit'),
    path('categeori_Edit_Save',views.categeori_edit_save,name='categeori_edit_save'),
    path('Fetch_categories',views.fetch_categori,name='fetch_categori'),
    path('Fetch_Templates',views.fetch_templates,name='fetch_templates'),
    path('categorie_List',views.categorie_list,name='categorie_list'),

    #=========Template urls=========
    path('Template_Form',views.template_load,name='template_load'),
    path('Template_List',views.template_list,name='template_list'),
    path('Template_Edit_List',views.template_editload,name='template_editload'),
    path('Template_save',views.template_save,name='template_save'),

    path('Account-Settings',views.profile,name='profile'),
    path('Account-Profile-Edit',views.useredit_save,name='useredit_save'),
    path('Account-Profile-Password-Edit',views.user_password_edit,name='user_password_edit'),
    path('Account-Profile-Password',views.userpassword_save,name='userpassword_save'),
  
    
    
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
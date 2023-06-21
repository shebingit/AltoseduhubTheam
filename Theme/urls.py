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
    path('Templates',views.TemplateView,name='TemplateView'),
    
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
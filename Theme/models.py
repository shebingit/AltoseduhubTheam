from django.db import models



#  Categorie Table 
class Categorie(models.Model):
    categorie_image = models.ImageField(null=True,blank = True,upload_to = 'categorie')
    categorie_name = models.CharField(max_length=255, null=True,blank=True,default='')
    status = models.CharField(max_length=255,null=True,blank=True,default=0)
    time = models.TimeField(max_length=100,null=True,blank=True)
    publish_date = models.DateField(max_length=255,null=True,blank=True)
    img_alttag = models.TextField(null=True,blank=True,default='')



class Templates(models.Model):
    categori_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True,default='')
    template_image = models.ImageField(null=True,blank = True,upload_to = 'templates_images')
    template_name = models.CharField(max_length=255, null=True,blank=True,default='')
    template_discription = models.TextField(null=True,blank=True,default='')
    template_status = models.CharField(max_length=255,null=True,blank=True,default=0)
    template_time = models.TimeField(max_length=100,null=True,blank=True)
    template_publish_date = models.DateField(max_length=255,null=True,blank=True)
    template_img_alttag = models.TextField(null=True,blank=True,default='')
    template_price =models.CharField(max_length=255,null=True,blank=True,default=0)
    template_rating=models.CharField(max_length=255,null=True,blank=True,default=0)
    video_file = models.FileField(upload_to='tempvideo/')
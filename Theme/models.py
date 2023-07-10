from django.db import models



#  Categorie Table 
class Categorie(models.Model):
    categorie_image = models.ImageField(null=True,blank = True,upload_to = 'categorie')
    categorie_name = models.CharField(max_length=255, null=True,blank=True,default='')
    status = models.CharField(max_length=255,null=True,blank=True,default=0)
    time = models.TimeField(max_length=100,null=True,blank=True)
    publish_date = models.DateField(max_length=255,null=True,blank=True)
    img_alttag = models.TextField(null=True,blank=True,default='')
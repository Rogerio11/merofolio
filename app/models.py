from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    categorie = models.CharField(max_length = 1500)
    
    def __str__(self):
        return self.categorie
        
class SiteWeb(models.Model):
    title = models.CharField(max_length = 1500)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    url = models.CharField(max_length = 1500)
    created_at = models.DateTimeField(auto_now_add=True)
    def upload_path(self, filename):
        return 'static/assets/images/%s_%s' % (self.created_at.strftime("%Y%m%d_%H%M%S"), filename)
    image = models.FileField(upload_to=upload_path, blank = True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    visible = models.IntegerField(default= 1)
    
    def __str__(self):
        return self.url
    
    def getParam(self):
        return str(self.id)+"-"+self.title.replace(" ","-")
    

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = RichTextField()
    author = models.CharField(max_length = 30)
    created_date = models.DateTimeField(auto_now=True )
    post_image = models.FileField(blank=True ,null =True , verbose_name="Add File")
 
    def __str__(self):
        return self.title 
    


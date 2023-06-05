from django.db import models

# Create your models here.

class Blog(models.Model):
  title = models.CharField( max_length=500)
  content = models.TextField(blank=True,null=True)
  author_name = models.CharField( max_length=500)
  creat_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  update_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title




from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Photo(models.Model):
    image = models.ImageField()
        
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    experiences = models.CharField(max_length=256, blank=False, default='')
    interests = models.CharField(max_length=256, blank=False, default='')
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)
    
        
class Log(models.Model):
    incidenttype = models.CharField(max_length=256, blank=False, default='')
    username = models.CharField(max_length=200,blank=False, default='')
    description = models.TextField()
    comment = models.TextField()
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    #GeoLocate Addition location
class Meta:
    ordering = ['created_on']

def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
        
class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="photo")

    content = models.TextField(max_length=2000)

    date_created = models.DateTimeField(auto_now_add=True) #DateTime Stamp

    def __str__(self):
        return self.content

class Meta:
    """Metadata."""

    ordering = ["-date_created"]

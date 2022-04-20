from django.db import models
 
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
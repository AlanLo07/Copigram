from django.db import models
# Create your models here.

class user(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
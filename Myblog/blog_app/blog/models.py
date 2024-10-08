from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Postes(models.Model):
    user_poste = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to='Images/')
    date_poste = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Admin(models.Model):
    name_admin = models.CharField(max_length=250)
    email_admin = models.CharField(max_length=200)
    password_admin = models.CharField(max_length=300)

class Post_admin(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="post_admin")
    name_admin = models.CharField(max_length=250)
    title = models.CharField(max_length=200)
    description = models.TextField()
    name_groupe = models.CharField(max_length=250)
    date_pub = models.DateTimeField()

class groupe(models.Model):
    name_groupe = models.CharField(max_length=250)
    folowers = models.IntegerField(max_length=100)
    pub = models.IntegerField()


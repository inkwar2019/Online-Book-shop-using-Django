from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    book_name = models.CharField(max_length = 100)
    book_description = models.TextField()
    post_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.book_name
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk': self.pk })

class Notification(models.Model):
    noti_name = models.CharField(max_length = 100)
    noti_body = models.TextField()
    noti_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    sender_author = models.CharField(max_length = 100)
    

    def __str__(self):
        return self.noti_name
    
    def get_absolute_url(self):
        return reverse('notification',kwargs={'pk': self.pk })